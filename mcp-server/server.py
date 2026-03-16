"""
nano-banana-slides MCP Server
提供五個工具：
  - list_layouts              列出所有可用版型
  - get_layout_prompt         取得版型的 Prompt 模版內容
  - analyze_company_template  解構公司 PPTX 模版的風格配色排版
  - build_presentation        根據投影片計劃生成 PPTX 草稿
  - generate_slide_images     呼叫 Gemini API 生成簡報格式圖片
"""
import sys
import json
import asyncio
from pathlib import Path

# 將 mcp-server 目錄加入 import 路徑
sys.path.insert(0, str(Path(__file__).parent))

from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"

mcp = FastMCP(
    name="nano-banana-slides",
    instructions="""
簡報版型 Prompt 庫 + PPTX 生成 MCP 伺服器。

可用工具：
1. list_layouts              — 列出所有版型分類與檔案名稱
2. get_layout_prompt         — 取得特定版型的完整 Prompt 模版
3. analyze_company_template  — 解構公司 PPTX 模版，提取風格規格
4. build_presentation        — 傳入投影片計劃 JSON，生成 .pptx 草稿
5. generate_slide_images     — 呼叫 Gemini API 生成簡報圖片（需 API key）

─── 工作流程 A（標準）───────────────────────────────────────────────────────
  用戶上傳來源資料 → AI 詢問規格需求
  → list_layouts 挑選適合版型
  → build_presentation 生成 PPTX
  → 上傳 Google Slides / NotebookLM 美化
  → （選用）generate_slide_images 生成圖片版

─── 工作流程 B（公司模版）────────────────────────────────────────────────────
  用戶上傳公司 PPTX 模版
  → analyze_company_template 解構風格配色
  → 結合來源資料與風格規格，挑選對應版型
  → build_presentation 生成符合公司風格的草稿
  → 同工作流程 A 後段
""",
)


@mcp.tool()
async def list_layouts() -> str:
    """
    列出所有可用的投影片版型分類與對應的 Prompt 模版檔案。

    回傳 JSON，格式：
    {
      "cover": ["basic-cover", "opl-photo-split-cover", ...],
      "bullet-points": [...],
      ...
    }

    build_presentation 支援的 layout 值：
      cover | closing | contents | section_divider | bullet_points | table
    """
    result = {}
    for cat in sorted(PROMPTS_DIR.iterdir()):
        if cat.is_dir() and not cat.name.startswith("."):
            files = sorted(f.stem for f in cat.glob("*.md") if not f.name.startswith("_"))
            if files:
                result[cat.name] = files
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
async def get_layout_prompt(category: str, filename: str) -> str:
    """
    取得特定版型的完整 Prompt 模版（含版面規格、Core Prompt、變數說明、程式碼骨架）。

    Args:
        category: 版型分類，例如 "cover"、"bullet-points"、"section-divider"、"contents"
        filename: 檔名（不含 .md），例如 "opl-photo-split-cover"、"opl-hierarchical-bullets"

    用 list_layouts 查看所有可用的 category / filename 組合。
    """
    path = PROMPTS_DIR / category / f"{filename}.md"
    if not path.exists():
        available = [
            str(p.relative_to(PROMPTS_DIR))
            for p in PROMPTS_DIR.rglob("*.md")
            if not p.name.startswith("_")
        ]
        return (
            f"找不到版型：{category}/{filename}.md\n\n"
            f"可用版型：\n" + "\n".join(f"  {a}" for a in sorted(available))
        )
    return path.read_text(encoding="utf-8")


@mcp.tool()
async def build_presentation(
    output_filename: str,
    slide_plan: str,
    output_dir: str = ".",
) -> str:
    """
    根據投影片計劃生成 PPTX 草稿檔案。

    Args:
        output_filename: 輸出檔名，例如 "公司簡介.pptx"
        output_dir:      輸出目錄（絕對路徑或相對路徑，預設當前目錄）
        slide_plan:      JSON 字串，投影片清單（見下方格式說明）

    ─── slide_plan 格式 ───────────────────────────────────────────────────────

    每張投影片為一個 JSON 物件，必須含 "layout" 欄位。

    支援的 layout 及對應欄位：

    ① cover（封面頁）
    {
      "layout": "cover",
      "brand_name_line_1": "MY BRAND",       // 右側色塊第一行大字
      "brand_name_line_2": "GROUP",           // 右側色塊第二行大字
      "main_title": "公司簡介 2026",           // 下半主標題
      "subtitle": "MY BRAND CO., LTD.",       // 副標題
      "logo_text": "MY BRAND",               // 左上角 Logo 文字
      "brand_color": "#1B4F9B",              // 品牌色（hex）
      "cta_text": "START",                   // 按鈕文字（可省略）
      "partner_text": "Partner of XYZ",      // 右下備注（可省略）
      "image_paths": [null, null, null]      // 三張照片路徑，null 用深色佔位塊
    }

    ② closing（結尾頁，與封面相同佈局）
    {
      "layout": "closing",
      "closing_primary": "感謝您",
      "closing_secondary": "Thank you",
      "logo_text": "MY BRAND",
      "brand_color": "#1B4F9B"
    }

    ③ contents（目錄頁）
    {
      "layout": "contents",
      "label_primary": "目錄",
      "label_secondary": "contents",
      "logo_text": "MY BRAND",
      "panel_color": "#2D415F",              // 左欄背景色（可省略）
      "items": [                             // 最多 6 項
        {"title": "公司背景", "subtitle": "BACKGROUND"},
        {"title": "主要業務", "subtitle": "SERVICES"},
        {"title": "合作夥伴", "subtitle": "PARTNERS"}
      ]
    }

    ④ section_divider（章節分隔頁）
    {
      "layout": "section_divider",
      "part_number": 1,                      // 章節編號（1–10）
      "section_title": "公司背景",
      "logo_text": "MY BRAND",
      "brand_color": "#1B4F9B",
      "accent_color": "#0091D5"              // 可省略
    }

    ⑤ bullet_points（條列式內容頁）
    {
      "layout": "bullet_points",
      "slide_title": "公司背景 — 基本資料",
      "logo_text": "MY BRAND",
      "accent_color": "#0091D5",             // 可省略
      "groups": [                            // 最多 3 組，每組最多 5 條
        {
          "title": "基本資料",
          "bullets": ["成立時間：2001 年", "員工：300 人", "總部：台北"]
        },
        {
          "title": "核心特色",
          "bullets": ["全球合作 60+ 國", "AEO 安全認證", "24/7 即時追蹤"]
        }
      ]
    }

    ⑥ table（表格頁）
    {
      "layout": "table",
      "slide_title": "服務方案比較",
      "logo_text": "MY BRAND",
      "accent_color": "#0091D5",
      "col_headers": ["項目", "基本版", "專業版", "企業版"],
      "rows_data": [
        ["倉儲空間", "500m²", "2,000m²", "無限制"],
        ["配送次數", "5次/月", "20次/月", "無限制"],
        ["客服支援", "email", "電話", "專屬顧問"]
      ]
    }

    ─── 完整範例 ───────────────────────────────────────────────────────────────

    slide_plan = '[
      {"layout":"cover","brand_name_line_1":"MY BRAND","brand_name_line_2":"GROUP",
       "main_title":"公司簡介 2026","subtitle":"MY BRAND CO., LTD.",
       "logo_text":"MY BRAND","brand_color":"#1B4F9B"},
      {"layout":"contents","label_primary":"目錄","label_secondary":"contents",
       "logo_text":"MY BRAND",
       "items":[{"title":"公司背景","subtitle":"BACKGROUND"},
                {"title":"主要業務","subtitle":"SERVICES"}]},
      {"layout":"section_divider","part_number":1,"section_title":"公司背景",
       "logo_text":"MY BRAND"},
      {"layout":"bullet_points","slide_title":"公司背景 — 基本資料",
       "logo_text":"MY BRAND",
       "groups":[{"title":"基本資料","bullets":["成立：2001年","員工：300人"]},
                 {"title":"核心特色","bullets":["全球網路","AEO認證"]}]},
      {"layout":"closing","closing_primary":"感謝您",
       "closing_secondary":"Thank you","logo_text":"MY BRAND"}
    ]'
    """
    from slide_builders import build_presentation_from_plan

    try:
        plan = json.loads(slide_plan)
    except json.JSONDecodeError as e:
        return f"❌ slide_plan JSON 格式錯誤：{e}\n請確認引號、括號完整。"

    if not isinstance(plan, list) or len(plan) == 0:
        return "❌ slide_plan 必須是非空的 JSON 陣列。"

    out_path = Path(output_dir).expanduser() / output_filename
    try:
        result = build_presentation_from_plan(plan, out_path)
        return (
            f"✅ 簡報已生成：{result}\n"
            f"共 {len(plan)} 張投影片\n"
            f"使用版型：{', '.join(s.get('layout','?') for s in plan)}"
        )
    except Exception as e:
        import traceback
        return f"❌ 生成失敗：{e}\n{traceback.format_exc()}"


@mcp.tool()
async def analyze_company_template(pptx_path: str) -> str:
    """
    解構公司 PPTX 模版，提取風格配色排版規格，供後續生成符合公司風格的簡報使用。

    Args:
        pptx_path: PPTX 模版的完整路徑（使用者上傳的公司簡報模版）

    回傳 JSON，包含：
      color_palette   色彩調色盤（hex list，依出現頻率排序）
      primary_color   主品牌色
      accent_color    強調色
      bg_color        背景色
      fonts           字型清單
      heading_size    推測標題字號
      body_size       推測內文字號
      layout_map      每頁推測版型（cover/section_divider/bullet_points/table/closing）
      style_prompt    給 AI 用的風格描述字串（可直接帶入 generate_slide_images）

    使用方式：
      1. 取得回傳的 style_spec JSON
      2. 將 style_spec 的色彩/字型應用到 build_presentation 的 slide_plan
         （修改 brand_color、accent_color 欄位）
      3. 將 style_spec 傳入 generate_slide_images 的 style_spec 參數
    """
    from template_analyzer import analyze_pptx_template

    path = Path(pptx_path).expanduser()
    if not path.exists():
        return f"❌ 找不到檔案：{pptx_path}"
    if path.suffix.lower() != ".pptx":
        return f"❌ 僅支援 .pptx 格式，收到：{path.suffix}"

    try:
        spec = analyze_pptx_template(str(path))
        result = json.dumps(spec, ensure_ascii=False, indent=2)
        return (
            f"✅ 模版分析完成：{path.name}\n"
            f"共 {spec['slide_count']} 張投影片\n"
            f"主色：{spec['primary_color']}  強調色：{spec['accent_color']}\n"
            f"字型：{', '.join(spec['fonts'][:3]) if spec['fonts'] else '未偵測到'}\n\n"
            f"完整規格：\n{result}"
        )
    except Exception as e:
        import traceback
        return f"❌ 分析失敗：{e}\n{traceback.format_exc()}"


@mcp.tool()
async def generate_slide_images(
    slide_plan: str,
    gemini_api_key: str,
    output_dir: str = ".",
    style_spec: str = "{}",
    model: str = "imagen-3.0-generate-001",
) -> str:
    """
    呼叫 Google Gemini / Imagen API，將投影片計劃轉換為簡報格式圖片（PNG）。

    Args:
        slide_plan:      JSON 字串，與 build_presentation 相同格式的投影片清單
        gemini_api_key:  Google AI Studio API key（前往 aistudio.google.com 取得）
        output_dir:      圖片輸出目錄（預設當前目錄）
        style_spec:      JSON 字串，analyze_company_template 的回傳結果（可省略）
                         省略時使用預設風格
        model:           生成模型（預設 imagen-3.0-generate-001）
                         備援：gemini-2.0-flash-exp

    每張投影片輸出一個 PNG 檔（slide_01.png、slide_02.png...）。
    圖片可直接上傳 Google Slides / NotebookLM / Canva 進行進一步美化。

    注意：
      - imagen-3.0 需要 Google AI Studio 帳號（免費配額有限）
      - 生成品質取決於 prompt 精確度；建議先用 build_presentation 確認結構再生成圖片
    """
    from gemini_exporter import generate_slide_images as _gen

    try:
        plan = json.loads(slide_plan)
    except json.JSONDecodeError as e:
        return f"❌ slide_plan JSON 格式錯誤：{e}"

    try:
        style = json.loads(style_spec) if style_spec.strip() not in ("{}", "") else {}
    except json.JSONDecodeError:
        style = {}

    if not gemini_api_key or not gemini_api_key.strip():
        return "❌ 請提供 Gemini API key（前往 aistudio.google.com 取得）"

    out_dir = Path(output_dir).expanduser()
    try:
        paths = _gen(
            slide_plan=plan,
            api_key=gemini_api_key.strip(),
            style_spec=style,
            output_dir=str(out_dir),
            model=model,
        )
        success = [p for p in paths if not p.startswith("[FAILED]")]
        failed  = [p for p in paths if p.startswith("[FAILED]")]

        msg = f"✅ 圖片生成完成：{len(success)}/{len(paths)} 張成功\n"
        msg += f"輸出目錄：{out_dir.resolve()}\n"
        if success:
            msg += "\n成功：\n" + "\n".join(f"  {p}" for p in success)
        if failed:
            msg += "\n失敗（已輸出 prompt 至 .txt）：\n" + "\n".join(f"  {p}" for p in failed)
        return msg

    except ImportError as e:
        return f"❌ {e}\n請執行：pip install google-genai"
    except Exception as e:
        import traceback
        return f"❌ 生成失敗：{e}\n{traceback.format_exc()}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
