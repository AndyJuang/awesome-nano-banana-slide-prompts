---
layout: cover
name: 三欄照片切割封面
tags: [cover, photo-grid, brand-block, split-layout]
source: 曜捷_公司簡介_簡報草稿_20260310.pptx — Slide 1
---

# 三欄照片切割封面 Prompt 模版

> 精確尺寸來源：實際 PPTX 解析（13.33" × 7.5"，16:9）

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│ [Logo 左上角 — 9pt]                                          │
│ ┌──────────┐ ┌──────────┐ ┌─────────────────────────────┐  │
│ │          │ │          │ │  ████████████████████████   │  │
│ │  Photo 1 │ │  Photo 2 │ │  BRAND NAME LINE 1  46pt    │  │
│ │          │ ├──────────┤ │  BRAND NAME LINE 2  46pt    │  │
│ │ (4.2"×   │ │  Photo 3 │ │  (6.83" × 4.5"  #1B4F9B)   │  │
│ │  4.5")   │ │          │ │                             │  │
│ └──────────┘ └──────────┘ └─────────────────────────────┘  │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │  主標題中文大字  38pt Bold         （白色底 full width）  │ │
│ │  英文副標題     17pt Bold                               │ │
│ │                              [ START / CTA ]   [ECU]   │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 版面精確規格

```
Slide: 13.33" × 7.50"

── 上半部（高 4.5"）──
Photo Block 1:  left=0.00"  top=0.00"  w=4.20"  h=4.50"  fill=#19325A
Photo Block 2:  left=4.35"  top=0.00"  w=2.05"  h=2.15"  fill=#0F3C6E
Photo Block 3:  left=4.35"  top=2.35"  w=2.05"  h=2.15"  fill=#0A234B
Brand Block:    left=6.50"  top=0.00"  w=6.83"  h=4.50"  fill=#1B4F9B

Logo Text:      left=0.20"  top=0.10"  w=6.00"  h=0.45"  9pt Bold white
Brand Line 1:   left=6.60"  top=0.70"  w=6.60"  h=1.10"  46pt Bold white
Brand Line 2:   left=6.60"  top=1.85"  w=6.60"  h=1.10"  46pt Bold white

── 下半部（y=4.55" 起，高 2.95"）──
Bottom White:   left=0.00"  top=4.55"  w=13.33"  h=2.95"  fill=#FFFFFF

Title CN:       left=0.80"  top=4.75"  w=11.70"  h=1.10"  38pt Bold #404040
Title EN:       left=0.80"  top=5.85"  w=11.70"  h=0.60"  17pt Bold #404040

CTA Button:     left=5.85"  top=6.72"  w=1.60"   h=0.45"  fill=#FFFFFF border=#CCC
CTA Text:       left=5.85"  top=6.74"  w=1.60"   h=0.38"  11pt center
Partner Logo:   left=10.50" top=6.90"  w=2.70"   h=0.38"  9pt right-align
```

## Core Prompt

```
Generate a presentation cover slide (16:9, 13.33" × 7.50"):

=== UPPER HALF (top 60% height = 4.5") ===

Left photo grid (occupies left 48.8% = 6.4" wide):
  Block A — top-left:
    Position: x=0, y=0, width=4.20", height=4.50"
    Fill: dark navy {photo_block_1_fill} (placeholder for image)
    Image: "{photo_1_description}"

  Block B — middle top:
    Position: x=4.35", y=0, width=2.05", height=2.15"
    Fill: darker navy {photo_block_2_fill}
    Image: "{photo_2_description}"

  Block C — middle bottom:
    Position: x=4.35", y=2.35", width=2.05", height=2.15"
    Fill: darkest navy {photo_block_3_fill}
    Image: "{photo_3_description}"

Right brand block:
  Position: x=6.50", y=0, width=6.83", height=4.50"
  Fill: brand navy {brand_color}
  Line 1 text: "{brand_name_line_1}" — 46pt, Bold, white, left-aligned, y≈0.70"
  Line 2 text: "{brand_name_line_2}" — 46pt, Bold, white, left-aligned, y≈1.85"

Logo / watermark (top-left overlay):
  Text: "{logo_text}" — 9pt, Bold, white, position x=0.20", y=0.10"

=== LOWER HALF (bottom 39% height = 2.95", white background) ===

Bottom area:
  Position: x=0, y=4.55", full width, height=2.95"
  Fill: white

Main title (Chinese/primary language):
  Text: "{main_title}" — 38pt, Bold, color={title_color}
  Position: x=0.80", y=4.75", width=11.70"

Subtitle (English/secondary):
  Text: "{subtitle}" — 17pt, Bold, color={subtitle_color}
  Position: x=0.80", y=5.85", width=11.70"

CTA button (optional):
  Rectangle: x=5.85", y=6.72", width=1.60", height=0.45", white fill, light border
  Label: "{cta_text}" — 11pt, centered, color={cta_text_color}

Partner/footnote text:
  Text: "{partner_text}" — 9pt, right-aligned, x=10.50", y=6.90"
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{photo_block_1_fill}` | 左大塊佔位色（或替換為照片） | `#19325A` |
| `{photo_block_2_fill}` | 中上塊佔位色 | `#0F3C6E` |
| `{photo_block_3_fill}` | 中下塊佔位色 | `#0A234B` |
| `{brand_color}` | 右側品牌色塊 | `#1B4F9B` |
| `{brand_name_line_1}` | 品牌名第一行 | `{brand_name_line_1}` |
| `{brand_name_line_2}` | 品牌名第二行 | `{brand_name_line_2}` |
| `{logo_text}` | 左上角 LOGO 文字 | `BRAND CO. 品牌公司` |
| `{main_title}` | 主標題（大字） | `品牌公司簡介` |
| `{title_color}` | 主標題顏色 | `#404040` |
| `{subtitle}` | 英文副標題 | `BRAND CO., LTD.` |
| `{subtitle_color}` | 副標題顏色 | `#404040` |
| `{cta_text}` | 按鈕文字 | `START` 或 `BEGIN` |
| `{partner_text}` | 夥伴/備注文字 | `Partner of XYZ` |
| `{photo_N_description}` | 照片描述（用於 AI 生圖或搜圖） | `aerial logistics warehouse photo` |

## python-pptx 程式碼骨架

```python
def build_photo_split_cover(prs, brand_name_1, brand_name_2, main_title, subtitle,
                             logo_text, cta_text="START", partner_text="",
                             brand_color=None, image_paths=None):
    """
    建立三欄照片切割封面

    Args:
        brand_name_1/2: 右側品牌名兩行
        main_title: 下半主標題（中文）
        subtitle: 副標題（英文）
        logo_text: 左上角 LOGO 文字
        brand_color: RGBColor，品牌色，預設 #1B4F9B
        image_paths: list[str|None]，三個照片路徑，None 用色塊替代
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    if brand_color is None:
        brand_color = RGBColor(0x1B, 0x4F, 0x9B)
    if image_paths is None:
        image_paths = [None, None, None]

    # — 照片區塊 —
    photo_specs = [
        (0.00, 0.00, 4.20, 4.50, 0x19, 0x32, 0x5A),
        (4.35, 0.00, 2.05, 2.15, 0x0F, 0x3C, 0x6E),
        (4.35, 2.35, 2.05, 2.15, 0x0A, 0x23, 0x4B),
    ]
    for i, (l, t, w, h, r, g, b) in enumerate(photo_specs):
        if image_paths[i]:
            slide.shapes.add_picture(
                image_paths[i], Inches(l), Inches(t), Inches(w), Inches(h))
        else:
            add_rect(slide, Inches(l), Inches(t), Inches(w), Inches(h),
                     fill_color=RGBColor(r, g, b))

    # — 品牌色塊（右側）—
    add_rect(slide, Inches(6.50), Inches(0), Inches(6.83), Inches(4.50),
             fill_color=brand_color)

    # — Logo 文字（左上）—
    add_text_box(slide, logo_text, Inches(0.20), Inches(0.10),
                 Inches(6.00), Inches(0.45), font_size=9, bold=True,
                 color=RGBColor(255, 255, 255))

    # — 品牌名（右側色塊上）—
    for line, top in [(brand_name_1, 0.70), (brand_name_2, 1.85)]:
        add_text_box(slide, line, Inches(6.60), Inches(top),
                     Inches(6.60), Inches(1.10), font_size=46, bold=True,
                     color=RGBColor(255, 255, 255), font_name="Calibri")

    # — 下半白底 —
    add_rect(slide, 0, Inches(4.55), prs.slide_width, Inches(2.95),
             fill_color=RGBColor(255, 255, 255))

    # — 主標題 —
    add_text_box(slide, main_title, Inches(0.80), Inches(4.75),
                 Inches(11.70), Inches(1.10), font_size=38, bold=True,
                 color=RGBColor(64, 64, 64))

    # — 英文副標題 —
    add_text_box(slide, subtitle, Inches(0.80), Inches(5.85),
                 Inches(11.70), Inches(0.60), font_size=17, bold=True,
                 color=RGBColor(64, 64, 64), font_name="Calibri")

    # — CTA 按鈕 —
    if cta_text:
        add_rect(slide, Inches(5.85), Inches(6.72), Inches(1.60), Inches(0.45),
                 fill_color=RGBColor(255, 255, 255),
                 border_color=RGBColor(180, 180, 180))
        add_text_box(slide, cta_text, Inches(5.85), Inches(6.74),
                     Inches(1.60), Inches(0.38), font_size=11,
                     align=PP_ALIGN.CENTER, font_name="Calibri")

    # — 夥伴/備注文字 —
    if partner_text:
        add_text_box(slide, partner_text, Inches(10.50), Inches(6.90),
                     Inches(2.70), Inches(0.38), font_size=9,
                     align=PP_ALIGN.RIGHT, font_name="Calibri")

    return slide
```

## 變體：結尾頁（Closing Slide）

結尾頁與封面共用相同佈局，差異如下：

| 元素 | 封面 | 結尾 |
|------|------|------|
| 主標題 | 公司/簡報名稱 | `感謝您` / `Thank You` |
| 主標題字號 | 38pt | 50pt |
| 副標題 | 英文公司名 | `Thank you` / `Q&A` |
| 副標題字號 | 17pt | 22pt |
| 按鈕文字 | `START` | `END` |

見 `cover/opl-style-closing.md` 獨立檔案。
