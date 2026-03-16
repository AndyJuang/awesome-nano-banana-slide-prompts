"""
gemini_exporter.py
使用 Gemini API 將投影片計劃轉換為簡報格式圖片。

支援兩種模型：
  - imagen-3.0-generate-001   高品質圖片生成（推薦）
  - gemini-2.0-flash-exp       文字+圖片多模態生成（備援）

輸出：
  每張投影片一個 PNG 檔，儲存至 output_dir
  命名格式：slide_01.png, slide_02.png ...
"""
import base64
import json
from pathlib import Path


# ── Prompt 工廠 ──────────────────────────────────────────────────────────────

def _build_slide_prompt(slide: dict, style: dict, slide_number: int) -> str:
    """將單張投影片的內容 + 風格規格轉換為 Gemini image prompt"""
    layout = slide.get("layout", "content").replace("_", " ")

    # 從 style_spec 提取
    primary   = style.get("primary_color",  "#1B4F9B")
    accent    = style.get("accent_color",   "#0091D5")
    bg        = style.get("bg_color",       "#FFFFFF")
    fonts     = style.get("fonts",          [])
    font_desc = fonts[0] if fonts else "sans-serif"
    heading_pt = style.get("heading_size",  24)
    body_pt    = style.get("body_size",     14)

    lines = [
        "Create a professional presentation slide image.",
        "Aspect ratio: 16:9. Resolution: 1920×1080px.",
        f"Slide number: {slide_number}. Layout type: {layout}.",
        "",
        "=== VISUAL STYLE ===",
        f"Primary brand color: {primary}",
        f"Accent color: {accent}",
        f"Background: {bg}",
        f"Font family: {font_desc}",
        f"Heading: {heading_pt}pt bold. Body: {body_pt}pt regular.",
        "Style: clean, corporate, modern. No decorative borders unless specified.",
        "",
        "=== SLIDE CONTENT ===",
    ]

    # 依版型描述內容
    if layout in ("cover", "closing"):
        lines += [
            f"Brand name line 1: '{slide.get('brand_name_line_1', '')}'",
            f"Brand name line 2: '{slide.get('brand_name_line_2', '')}'",
            f"Main title: '{slide.get('main_title') or slide.get('closing_primary', '')}'",
            f"Subtitle: '{slide.get('subtitle') or slide.get('closing_secondary', '')}'",
            f"Logo text (small, top corner): '{slide.get('logo_text', '')}'",
            "Layout: left 48% photo grid (3 stacked blocks), right 52% solid brand color block with brand name in white.",
            "Bottom quarter: white background with main title (large) and subtitle.",
        ]

    elif layout == "contents":
        items = slide.get("items", [])
        item_lines = "\n".join(
            f"  {i+1}. {it.get('title','')} — {it.get('subtitle','')}"
            for i, it in enumerate(items)
        )
        lines += [
            "Layout: left dark panel (43% width) with primary label, right side numbered list.",
            f"Left panel label: '{slide.get('label_primary','目錄')} / {slide.get('label_secondary','contents')}' in white.",
            f"Right side numbered items:\n{item_lines}",
            "Each item has a colored badge (alternating brand/gray), title, subtitle, and thin separator line.",
        ]

    elif layout == "section divider":
        lines += [
            "Layout: light gray full background.",
            f"Left side: large solid brand-colored square block with 'P' (large, ~68pt) and 'ART {slide.get('part_number',1):02d}' label.",
            f"Below the block: hollow outline square (decorative).",
            f"Right side: section title '{slide.get('section_title','')}' in 34pt bold with accent-colored underline.",
            f"Bottom right corner: small badge with '{_chapter_label(slide.get('part_number',1))}' in white on brand color.",
        ]

    elif layout == "bullet points":
        groups = slide.get("groups", [])
        group_lines = []
        for g in groups:
            group_lines.append(f"  Section: '{g.get('title','')}'")
            for b in g.get("bullets", []):
                group_lines.append(f"    • {b}")
        lines += [
            f"Slide title: '{slide.get('slide_title','')}' with accent dot and underline.",
            "Content area: hierarchical layout with section headers (thick accent vertical bar + bold text) and bullet items (small accent squares).",
            "Groups:\n" + "\n".join(group_lines),
            "Top-right: decorative cluster of 3 colored squares (brand navy, accent blue, white outline).",
            "Bottom: thin light-blue accent rule.",
        ]

    elif layout == "table":
        headers = slide.get("col_headers", [])
        rows    = slide.get("rows_data", [])
        lines += [
            f"Slide title: '{slide.get('slide_title','')}'",
            f"Table: {len(rows)} data rows × {len(headers)} columns.",
            f"Column headers: {headers}",
            "Header row: accent color background, white bold text.",
            "Alternating row colors: white / very light blue.",
            "Left column: slightly emphasized (bold or accent color text).",
        ]

    else:
        # Generic fallback
        lines += [json.dumps(slide, ensure_ascii=False)]

    lines += [
        "",
        "=== REQUIREMENTS ===",
        "Do NOT include any UI chrome, browser frames, or watermarks.",
        "Do NOT add page numbers unless specified.",
        "Text must be readable at 1080p. Maintain generous whitespace.",
        "Output ONLY the slide image, no surrounding context.",
    ]

    return "\n".join(lines)


def _chapter_label(n: int) -> str:
    labels = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN"]
    return labels[n - 1] if 1 <= n <= len(labels) else str(n)


# ── Gemini 呼叫 ──────────────────────────────────────────────────────────────

def generate_slide_images(
    slide_plan: list[dict],
    api_key: str,
    style_spec: dict,
    output_dir: str = ".",
    model: str = "imagen-3.0-generate-001",
) -> list[str]:
    """
    為 slide_plan 中的每張投影片呼叫 Gemini API 生成圖片。

    Args:
        slide_plan:  投影片清單（與 build_presentation 相同格式）
        api_key:     Google AI Studio API key
        style_spec:  analyze_company_template 回傳的風格規格，或空 dict
        output_dir:  圖片儲存目錄
        model:       Gemini/Imagen 模型名稱

    Returns:
        已儲存的圖片路徑清單
    """
    try:
        from google import genai
        from google.genai import types as gtypes
    except ImportError:
        raise ImportError(
            "請安裝 google-genai：pip install google-genai"
        )

    client = genai.Client(api_key=api_key)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    saved_paths = []

    for i, slide in enumerate(slide_plan):
        prompt = _build_slide_prompt(slide, style_spec, i + 1)
        out_path = out_dir / f"slide_{i+1:02d}.png"

        try:
            if "imagen" in model:
                # Imagen 3 — 專用圖片生成
                response = client.models.generate_images(
                    model=model,
                    prompt=prompt,
                    config=gtypes.GenerateImagesConfig(
                        number_of_images=1,
                        aspect_ratio="16:9",
                        output_mime_type="image/png",
                    ),
                )
                img_bytes = response.generated_images[0].image.image_bytes

            else:
                # Gemini Flash — 多模態生成（備援）
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                    config=gtypes.GenerateContentConfig(
                        response_modalities=["IMAGE", "TEXT"],
                    ),
                )
                img_bytes = None
                for part in response.candidates[0].content.parts:
                    if hasattr(part, "inline_data") and part.inline_data:
                        img_bytes = base64.b64decode(part.inline_data.data)
                        break
                if img_bytes is None:
                    raise ValueError("Gemini 未回傳圖片內容")

            out_path.write_bytes(img_bytes)
            saved_paths.append(str(out_path.resolve()))

        except Exception as e:
            # 生成失敗時建立純文字描述檔作為佔位
            fallback = out_path.with_suffix(".txt")
            fallback.write_text(
                f"Slide {i+1} generation failed: {e}\n\nPrompt:\n{prompt}",
                encoding="utf-8",
            )
            saved_paths.append(f"[FAILED] {fallback}")

    return saved_paths
