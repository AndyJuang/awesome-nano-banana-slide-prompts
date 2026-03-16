"""
slide_builders.py
各版型的 python-pptx 實作函式
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pathlib import Path

SLIDE_WIDTH  = Inches(13.33)
SLIDE_HEIGHT = Inches(7.50)

CHAPTER_LABELS = [
    "ONE","TWO","THREE","FOUR","FIVE",
    "SIX","SEVEN","EIGHT","NINE","TEN",
]

# ── 色彩工具 ────────────────────────────────────────────────────────────────

def parse_color(val, default=(0x1B, 0x4F, 0x9B)) -> RGBColor:
    """接受 '#RRGGBB'、(r,g,b) tuple 或 RGBColor"""
    if isinstance(val, RGBColor):
        return val
    if isinstance(val, str):
        h = val.lstrip("#")
        if len(h) == 6:
            return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))
    if isinstance(val, (list, tuple)) and len(val) == 3:
        return RGBColor(*val)
    return RGBColor(*default)

# ── 基礎元素 ────────────────────────────────────────────────────────────────

def add_rect(slide, left, top, width, height,
             fill_color=None, border_color=None, border_width=Pt(1)):
    shape = slide.shapes.add_shape(1, int(left), int(top), int(width), int(height))
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = border_width
    else:
        shape.line.fill.background()
    return shape


def add_text(slide, text, left, top, width, height,
             font_size=14, bold=False, color=None,
             align=PP_ALIGN.LEFT, font_name="Microsoft JhengHei"):
    box = slide.shapes.add_textbox(int(left), int(top), int(width), int(height))
    tf  = box.text_frame
    tf.word_wrap = True
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.name = font_name
    if color:
        run.font.color.rgb = color
    return box

# ── 版型實作 ─────────────────────────────────────────────────────────────────

def _build_cover_or_closing(slide, s: dict):
    """封面頁 & 結尾頁（共用結構，is_closing 由 layout 欄位判斷）"""
    is_closing   = s.get("layout") == "closing"
    brand_color  = parse_color(s.get("brand_color", "#1B4F9B"))
    logo_text    = s.get("logo_text", "{brand_name}")
    image_paths  = s.get("image_paths") or [None, None, None]

    # — 左側三塊照片佔位色 —
    photo_specs = [
        (0.00, 0.00, 4.20, 4.50, 0x19, 0x32, 0x5A),
        (4.35, 0.00, 2.05, 2.15, 0x0F, 0x3C, 0x6E),
        (4.35, 2.35, 2.05, 2.15, 0x0A, 0x23, 0x4B),
    ]
    for i, (l, t, w, h, r, g, b) in enumerate(photo_specs):
        img = image_paths[i] if i < len(image_paths) else None
        if img and Path(img).exists():
            slide.shapes.add_picture(img, Inches(l), Inches(t), Inches(w), Inches(h))
        else:
            add_rect(slide, Inches(l), Inches(t), Inches(w), Inches(h),
                     fill_color=RGBColor(r, g, b))

    # — 右側品牌色塊 —
    add_rect(slide, Inches(6.50), 0, Inches(6.83), Inches(4.50), fill_color=brand_color)

    # — 左上角 Logo —
    add_text(slide, logo_text, Inches(0.20), Inches(0.10), Inches(6.00), Inches(0.45),
             font_size=9, bold=True, color=RGBColor(255,255,255), font_name="Calibri")

    # — 品牌名（封面才顯示）—
    if not is_closing:
        for line, top in [
            (s.get("brand_name_line_1",""), 0.70),
            (s.get("brand_name_line_2",""), 1.85),
        ]:
            if line:
                add_text(slide, line, Inches(6.60), Inches(top),
                         Inches(6.60), Inches(1.10),
                         font_size=46, bold=True,
                         color=RGBColor(255,255,255), font_name="Calibri")

    # — 下半白底 —
    add_rect(slide, 0, Inches(4.55), SLIDE_WIDTH, Inches(2.95),
             fill_color=RGBColor(255,255,255))

    # — 主標題 —
    main_title = s.get("closing_primary","感謝您") if is_closing else s.get("main_title","")
    main_size  = 50 if is_closing else 38
    add_text(slide, main_title, Inches(0.80), Inches(4.65),
             Inches(11.70), Inches(1.10),
             font_size=main_size, bold=True, color=RGBColor(64,64,64))

    # — 副標題 —
    subtitle  = s.get("closing_secondary","Thank you") if is_closing else s.get("subtitle","")
    sub_size  = 22 if is_closing else 17
    sub_top   = 5.75 if is_closing else 5.85
    if subtitle:
        add_text(slide, subtitle, Inches(0.80), Inches(sub_top),
                 Inches(11.70), Inches(0.60),
                 font_size=sub_size, bold=True,
                 color=RGBColor(64,64,64), font_name="Calibri")

    # — CTA 按鈕 —
    cta   = "END" if is_closing else s.get("cta_text","START")
    btn_x = Inches(5.70) if is_closing else Inches(5.85)
    btn_w = Inches(1.90) if is_closing else Inches(1.60)
    add_rect(slide, btn_x, Inches(6.72), btn_w, Inches(0.45),
             fill_color=RGBColor(255,255,255), border_color=RGBColor(180,180,180))
    add_text(slide, cta, btn_x, Inches(6.74), btn_w, Inches(0.38),
             font_size=12 if is_closing else 11,
             align=PP_ALIGN.CENTER, font_name="Calibri")

    # — 夥伴/備注文字 —
    partner = s.get("partner_text","")
    if partner:
        add_text(slide, partner, Inches(10.50), Inches(6.90),
                 Inches(2.70), Inches(0.38),
                 font_size=9, align=PP_ALIGN.RIGHT, font_name="Calibri")


def _build_contents(slide, s: dict):
    """深色左欄數字徽章目錄"""
    panel_color  = parse_color(s.get("panel_color",     "#2D415F"))
    badge_odd    = parse_color(s.get("badge_color_odd",  "#1B4F9B"))
    badge_even   = parse_color(s.get("badge_color_even", "#808080"))
    logo_text    = s.get("logo_text", "{brand_name}")

    # 左欄
    add_rect(slide, 0, 0, Inches(5.80), SLIDE_HEIGHT, fill_color=panel_color)
    add_rect(slide, Inches(0.35), Inches(2.70), Inches(0.32), Inches(0.32),
             fill_color=RGBColor(0x1B,0x4F,0x9B))
    add_rect(slide, Inches(0.75), Inches(2.90), Inches(0.22), Inches(0.22),
             fill_color=RGBColor(0x00,0x91,0xD5))

    add_text(slide, s.get("label_primary","目錄"),
             Inches(0.50), Inches(2.85), Inches(4.50), Inches(0.85),
             font_size=34, bold=True, color=RGBColor(255,255,255))
    add_text(slide, s.get("label_secondary","contents"),
             Inches(0.50), Inches(3.65), Inches(4.50), Inches(0.60),
             font_size=20, bold=True, color=RGBColor(255,255,255), font_name="Calibri")

    # 目錄項目
    BADGE_W = Inches(0.58)
    for i, item in enumerate(s.get("items",[])[:6]):
        y = Inches(0.35) + Inches(1.12) * i
        bc = badge_odd if i % 2 == 0 else badge_even

        add_rect(slide, Inches(6.10), y, BADGE_W, BADGE_W, fill_color=bc)
        add_text(slide, str(i+1),
                 Inches(6.10), y + Inches(0.08), BADGE_W, Inches(0.45),
                 font_size=18, bold=True, color=RGBColor(255,255,255),
                 align=PP_ALIGN.CENTER, font_name="Calibri")

        add_text(slide, item.get("title",""),
                 Inches(6.10) + BADGE_W + Inches(0.22), y,
                 Inches(6.00), Inches(0.38),
                 font_size=16, bold=True, color=RGBColor(64,64,64))

        if item.get("subtitle"):
            add_text(slide, item["subtitle"],
                     Inches(6.10) + BADGE_W + Inches(0.22), y + Inches(0.37),
                     Inches(6.00), Inches(0.26),
                     font_size=10, color=RGBColor(128,128,128), font_name="Calibri")

        add_rect(slide, Inches(6.10), y + Inches(0.68),
                 Inches(6.80), Inches(0.025),
                 fill_color=RGBColor(240,240,240))

    # 右下 Logo
    add_text(slide, logo_text, Inches(11.30), Inches(7.10),
             Inches(1.90), Inches(0.32),
             font_size=9, bold=True, color=RGBColor(0x1B,0x4F,0x9B), font_name="Calibri")


def _build_section_divider(slide, s: dict):
    """PART 徽章章節分隔頁"""
    badge_color  = parse_color(s.get("brand_color",  "#1B4F9B"))
    accent_color = parse_color(s.get("accent_color", "#0091D5"))
    logo_text    = s.get("logo_text", "{brand_name}")
    part_number  = int(s.get("part_number", 1))
    section_title = s.get("section_title", "")

    # 淺灰背景
    add_rect(slide, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT,
             fill_color=RGBColor(0xF8,0xF8,0xF8))

    # 右上 Logo
    add_text(slide, logo_text, Inches(11.30), Inches(0.08),
             Inches(1.90), Inches(0.45),
             font_size=9, bold=True, color=badge_color, font_name="Calibri")

    # PART 徽章
    add_rect(slide, Inches(1.40), Inches(1.70), Inches(2.60), Inches(2.70),
             fill_color=badge_color)
    add_text(slide, "P", Inches(1.50), Inches(1.80), Inches(1.00), Inches(1.30),
             font_size=68, bold=True, color=RGBColor(255,255,255))
    add_text(slide, f"ART {part_number:02d}",
             Inches(2.40), Inches(3.10), Inches(1.50), Inches(0.55),
             font_size=20, bold=True, color=RGBColor(255,255,255), font_name="Calibri")

    # 空心輪廓方塊
    add_rect(slide, Inches(1.65), Inches(4.55), Inches(1.50), Inches(1.50),
             fill_color=RGBColor(255,255,255), border_color=badge_color)

    # 右側標題
    add_rect(slide, Inches(4.70), Inches(2.95), Inches(0.25), Inches(0.25),
             fill_color=accent_color)
    add_text(slide, section_title, Inches(5.10), Inches(2.68),
             Inches(7.50), Inches(0.85),
             font_size=34, bold=True, color=RGBColor(64,64,64))
    add_rect(slide, Inches(5.10), Inches(3.60), Inches(6.80), Inches(0.06),
             fill_color=accent_color)

    # 右下角英文章節標籤
    label = (CHAPTER_LABELS[part_number-1]
             if 1 <= part_number <= len(CHAPTER_LABELS)
             else str(part_number))
    add_rect(slide, Inches(11.95), Inches(6.82), Inches(1.38), Inches(0.50),
             fill_color=badge_color)
    add_text(slide, label, Inches(11.95), Inches(6.84),
             Inches(1.38), Inches(0.42),
             font_size=13, bold=True, color=RGBColor(255,255,255),
             align=PP_ALIGN.CENTER, font_name="Calibri")


def _build_bullet_points(slide, s: dict):
    """階層式條列內容頁（兩層：分組標題 + 子項目）"""
    accent_color = parse_color(s.get("accent_color", "#0091D5"))
    logo_text    = s.get("logo_text", "{brand_name}")
    slide_title  = s.get("slide_title", "")
    groups       = s.get("groups", [])

    NAVY  = RGBColor(0x1B,0x4F,0x9B)
    DARK  = RGBColor(64,64,64)
    WHITE = RGBColor(255,255,255)

    # 右上裝飾
    add_text(slide, logo_text, Inches(11.30), Inches(0.08),
             Inches(1.90), Inches(0.45),
             font_size=9, bold=True, color=NAVY, font_name="Calibri")
    add_rect(slide, Inches(12.25), Inches(0.22), Inches(0.38), Inches(0.38), fill_color=NAVY)
    add_rect(slide, Inches(11.90), Inches(0.45), Inches(0.24), Inches(0.24), fill_color=accent_color)
    add_rect(slide, Inches(12.58), Inches(0.52), Inches(0.19), Inches(0.19),
             fill_color=WHITE, border_color=RGBColor(180,180,180))

    # 標題列
    add_rect(slide, Inches(0.38), Inches(0.75), Inches(0.22), Inches(0.22), fill_color=accent_color)
    add_text(slide, slide_title, Inches(0.72), Inches(0.62),
             Inches(11.00), Inches(0.58),
             font_size=24, bold=True, color=DARK)
    add_rect(slide, Inches(0.38), Inches(1.28), Inches(12.00), Inches(0.04), fill_color=accent_color)

    # 內容區
    y = Inches(1.50)
    for group in groups[:3]:
        add_rect(slide, Inches(0.38), y, Inches(0.16), Inches(0.30), fill_color=accent_color)
        add_text(slide, group.get("title",""), Inches(0.66), y,
                 Inches(12.00), Inches(0.42),
                 font_size=15, bold=True, color=DARK)
        y += Inches(0.57)

        for bullet in group.get("bullets",[])[:5]:
            add_rect(slide, Inches(0.55), y + Inches(0.15),
                     Inches(0.10), Inches(0.10), fill_color=accent_color)
            add_text(slide, bullet, Inches(0.78), y,
                     Inches(12.00), Inches(0.40),
                     font_size=14, color=DARK)
            y += Inches(0.44)
        y += Inches(0.50)

    # 底部裝飾線
    add_rect(slide, Inches(0.38), Inches(7.18), Inches(12.60), Inches(0.05),
             fill_color=RGBColor(0xE8,0xF4,0xFD))


def _build_table(slide, s: dict):
    """基礎表格頁"""
    accent_color = parse_color(s.get("accent_color", "#0091D5"))
    light_row    = parse_color(s.get("even_row_color", "#E8F4FD"))
    logo_text    = s.get("logo_text", "{brand_name}")
    slide_title  = s.get("slide_title", "")
    col_headers  = s.get("col_headers", [])
    rows_data    = s.get("rows_data", [])

    NAVY  = RGBColor(0x1B,0x4F,0x9B)
    DARK  = RGBColor(64,64,64)
    WHITE = RGBColor(255,255,255)

    add_text(slide, logo_text, Inches(11.30), Inches(0.08),
             Inches(1.90), Inches(0.45),
             font_size=9, bold=True, color=NAVY, font_name="Calibri")
    add_rect(slide, Inches(0.38), Inches(0.45), Inches(0.12), Inches(0.50),
             fill_color=accent_color)
    add_text(slide, slide_title, Inches(0.58), Inches(0.40),
             SLIDE_WIDTH - Inches(1.00), Inches(0.60),
             font_size=22, bold=True, color=DARK)

    if not col_headers or not rows_data:
        return

    tbl = slide.shapes.add_table(
        len(rows_data) + 1, len(col_headers),
        Inches(0.40), Inches(1.30),
        SLIDE_WIDTH - Inches(0.80), SLIDE_HEIGHT - Inches(1.80),
    ).table

    for ci, header in enumerate(col_headers):
        cell = tbl.cell(0, ci)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = accent_color
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.runs[0] if p.runs else p.add_run()
        run.font.bold  = True
        run.font.color.rgb = WHITE
        run.font.size  = Pt(14)

    for ri, row in enumerate(rows_data):
        bg = light_row if ri % 2 == 1 else WHITE
        for ci, val in enumerate(row):
            cell = tbl.cell(ri + 1, ci)
            cell.text = str(val)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if ci == 0 else PP_ALIGN.CENTER
            run = p.runs[0] if p.runs else p.add_run()
            run.font.size  = Pt(13)
            run.font.color.rgb = DARK


# ── 版型路由表 ────────────────────────────────────────────────────────────────

LAYOUT_BUILDERS = {
    "cover":           _build_cover_or_closing,
    "closing":         _build_cover_or_closing,
    "contents":        _build_contents,
    "section_divider": _build_section_divider,
    "bullet_points":   _build_bullet_points,
    "table":           _build_table,
}

# ── 公開入口 ──────────────────────────────────────────────────────────────────

def build_presentation_from_plan(plan: list[dict], output_path) -> str:
    """
    根據 slide plan 生成 PPTX。

    Args:
        plan: 投影片清單，每項為 dict，必須含 "layout" 欄位
        output_path: 輸出路徑（str 或 Path）

    Returns:
        絕對路徑字串
    """
    prs = Presentation()
    prs.slide_width  = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank = prs.slide_layouts[6]

    for s in plan:
        layout  = s.get("layout","").lower().replace("-","_")
        builder = LAYOUT_BUILDERS.get(layout)
        slide   = prs.slides.add_slide(blank)

        if builder:
            builder(slide, s)
        else:
            add_text(slide,
                     f"[未支援的版型: {layout}]\n支援：{', '.join(LAYOUT_BUILDERS)}",
                     Inches(1), Inches(3), Inches(11), Inches(1.5),
                     font_size=18, color=RGBColor(200,0,0))

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out))
    return str(out.resolve())
