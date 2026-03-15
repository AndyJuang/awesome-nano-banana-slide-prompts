---
layout: section-divider
name: PART 徽章章節分隔頁
tags: [section-divider, part-badge, light-bg, chapter-label]
source: 曜捷_公司簡介_簡報草稿_20260310.pptx — Slides 3,5,7,9,11,13
---

# PART 徽章章節分隔頁 Prompt 模版

> 精確尺寸來源：實際 PPTX 解析（13.33" × 7.5"，16:9）

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│                                    [Logo 右上 9pt]           │
│                                                              │
│    ┌──────────────────────────────────────────────────────┐  │
│    │  ┌─────────────┐   ■ (4.7", 2.95")                  │  │
│    │  │  P   68pt   │   章節標題  34pt Bold               │  │
│    │  │  ART 0X     │   ─────────────────────────         │  │
│    │  │  20pt Bold  │                                      │  │
│    │  │ 2.6"×2.7"   │                                      │  │
│    │  │  #1B4F9B    │                                      │  │
│    │  └─────────────┘                                      │  │
│    │  ┌─────────────┐                                      │  │
│    │  │  空心白色    │                                      │  │
│    │  │ 1.5"×1.5"   │                                      │  │
│    │  └─────────────┘                                      │  │
│    └──────────────────────────────────────────────────────┘  │
│                               [英文章節標籤  #1B4F9B 右下角]  │
└─────────────────────────────────────────────────────────────┘
```

## 版面精確規格

```
Slide: 13.33" × 7.50"
Background: full slide fill #F8F8F8 (極淺灰)

── 右上角 Logo ──
Logo Text:    left=11.30"  top=0.08"  w=1.90"  h=0.45"  9pt Bold brand color

── 左側 PART 徽章組 ──
Navy Block:   left=1.40"  top=1.70"  w=2.60"  h=2.70"  fill=#1B4F9B
  "P" Text:   left=1.50"  top=1.80"  w=1.00"  h=1.30"  68pt Bold white
  "ART 0X":   left=2.40"  top=3.10"  w=1.50"  h=0.55"  20pt Bold white

Hollow Square: left=1.65"  top=4.55"  w=1.50"  h=1.50"
               fill=white  border=brand color  (空心輪廓)

── 右側標題區 ──
Accent Dot:   left=4.70"  top=2.95"  w=0.25"  h=0.25"  fill=#0091D5
Title Text:   left=5.10"  top=2.68"  w=7.50"  h=0.85"  34pt Bold #404040
Underline:    left=5.10"  top=3.60"  w=6.80"  h=0.06"  fill=#0091D5

── 右下角章節英文標籤 ──
Badge Rect:   left=11.95"  top=6.82"  w=1.38"  h=0.50"  fill=#1B4F9B
Badge Text:   left=11.95"  top=6.84"  w=1.38"  h=0.42"  13pt Bold white center
  Values: ONE / TWO / THREE / FOUR / FIVE / SIX / SEVEN / EIGHT ...
```

## Core Prompt

```
Generate a section divider slide (16:9, 13.33" × 7.50"):

Background: full-slide rectangle, fill={bg_color} (very light gray)

=== TOP RIGHT LOGO ===
Text: "{logo_text}" — 9pt, Bold, {logo_color}
Position: x=11.30", y=0.08", width=1.90"

=== LEFT — PART BADGE GROUP ===

Main navy block:
  Rectangle: x=1.40", y=1.70", width=2.60", height=2.70"
  Fill: {badge_fill_color}

  Inside — "P" letter:
    Text: "P" — 68pt, Bold, white
    Position: x=1.50", y=1.80", width=1.00", height=1.30"

  Inside — "ART 0X" label:
    Text: "ART {part_number_padded}" — 20pt, Bold, white
    Position: x=2.40", y=3.10", width=1.50", height=0.55"
    part_number_padded: zero-padded 2 digits e.g. "01", "02" ... "09", "10"

Hollow outline square (below navy block):
  Rectangle: x=1.65", y=4.55", width=1.50", height=1.50"
  Fill: white (or transparent)
  Border: {outline_color}, weight=1.5pt

=== RIGHT — SECTION TITLE ===

Accent dot:
  Square: x=4.70", y=2.95", size=0.25"×0.25"
  Fill: {accent_dot_color}

Section title text:
  Text: "{section_title}" — 34pt, Bold, {title_color}
  Position: x=5.10", y=2.68", width=7.50", height=0.85"

Underline bar:
  Rectangle: x=5.10", y=3.60", width=6.80", height=0.06"
  Fill: {underline_color}

=== BOTTOM RIGHT — CHAPTER LABEL ===

Badge rectangle:
  Position: x=11.95", y=6.82", width=1.38", height=0.50"
  Fill: {chapter_badge_color}

Badge text:
  Text: "{chapter_label_en}" — 13pt, Bold, white, centered
  Position: x=11.95", y=6.84", width=1.38", height=0.42"
  Options: ONE / TWO / THREE / FOUR / FIVE / SIX ...
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{bg_color}` | 全頁背景色（淺灰） | `#F8F8F8` |
| `{logo_text}` | 右上 Logo 文字 | `{brand_name}` |
| `{logo_color}` | Logo 文字色 | `#1B4F9B` |
| `{badge_fill_color}` | PART 徽章主色 | `#1B4F9B` |
| `{part_number_padded}` | 章節編號（補零） | `01` / `02` ... `10` |
| `{outline_color}` | 空心方塊邊框色 | `#1B4F9B` 或 `#0091D5` |
| `{accent_dot_color}` | 標題旁圓點色 | `#0091D5` |
| `{section_title}` | 章節中文標題 | `集團背景概覽` |
| `{title_color}` | 標題文字色 | `#404040` |
| `{underline_color}` | 標題下方線條色 | `#0091D5` |
| `{chapter_badge_color}` | 右下角徽章底色 | `#1B4F9B` |
| `{chapter_label_en}` | 英文章節標籤 | `ONE` / `TWO` / `THREE` |
| `{brand_name}` | 品牌名稱（用於 Logo 文字） | `{brand_name}` |
| `{subsidiary_name_cn}` | 子公司中文名稱（用於章節標題範例） | `{subsidiary_name_cn}` |

## 章節編號對照表

| part_number | part_number_padded | chapter_label_en |
|------------|-------------------|-----------------|
| 1 | `01` | `ONE` |
| 2 | `02` | `TWO` |
| 3 | `03` | `THREE` |
| 4 | `04` | `FOUR` |
| 5 | `05` | `FIVE` |
| 6 | `06` | `SIX` |
| 7 | `07` | `SEVEN` |
| 8 | `08` | `EIGHT` |

## python-pptx 程式碼骨架

```python
CHAPTER_LABELS = ["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN"]

def build_part_badge_divider(prs, part_number, section_title,
                              badge_color=None, accent_color=None, logo_text="BRAND"):
    """
    建立 PART 徽章章節分隔頁

    Args:
        part_number: 章節編號 (int, 1-based)
        section_title: 章節中文標題
        badge_color: RGBColor，PART 徽章色，預設 #1B4F9B
        accent_color: RGBColor，強調色（點、底線），預設 #0091D5
        logo_text: 右上角 Logo 文字
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN

    slide = prs.slides.add_slide(prs.slide_layouts[6])

    if badge_color is None:
        badge_color = RGBColor(0x1B, 0x4F, 0x9B)
    if accent_color is None:
        accent_color = RGBColor(0x00, 0x91, 0xD5)

    # 全頁淺灰背景
    add_rect(slide, 0, 0, prs.slide_width, prs.slide_height,
             fill_color=RGBColor(0xF8, 0xF8, 0xF8))

    # 右上 Logo
    add_text_box(slide, logo_text, Inches(11.30), Inches(0.08),
                 Inches(1.90), Inches(0.45), font_size=9, bold=True,
                 color=badge_color, font_name="Calibri")

    # PART 深藍方塊
    add_rect(slide, Inches(1.40), Inches(1.70), Inches(2.60), Inches(2.70),
             fill_color=badge_color)

    # "P" 大字
    add_text_box(slide, "P", Inches(1.50), Inches(1.80),
                 Inches(1.00), Inches(1.30), font_size=68, bold=True,
                 color=RGBColor(255, 255, 255))

    # "ART 0X"
    part_str = f"ART {part_number:02d}"
    add_text_box(slide, part_str, Inches(2.40), Inches(3.10),
                 Inches(1.50), Inches(0.55), font_size=20, bold=True,
                 color=RGBColor(255, 255, 255), font_name="Calibri")

    # 空心輪廓方塊
    add_rect(slide, Inches(1.65), Inches(4.55), Inches(1.50), Inches(1.50),
             fill_color=RGBColor(255, 255, 255), border_color=badge_color)

    # 右側強調點
    add_rect(slide, Inches(4.70), Inches(2.95), Inches(0.25), Inches(0.25),
             fill_color=accent_color)

    # 章節標題
    add_text_box(slide, section_title, Inches(5.10), Inches(2.68),
                 Inches(7.50), Inches(0.85), font_size=34, bold=True,
                 color=RGBColor(64, 64, 64))

    # 標題底線
    add_rect(slide, Inches(5.10), Inches(3.60), Inches(6.80), Inches(0.06),
             fill_color=accent_color)

    # 右下角章節英文標籤
    label = CHAPTER_LABELS[part_number - 1] if part_number <= len(CHAPTER_LABELS) else str(part_number)
    add_rect(slide, Inches(11.95), Inches(6.82), Inches(1.38), Inches(0.50),
             fill_color=badge_color)
    add_text_box(slide, label, Inches(11.95), Inches(6.84),
                 Inches(1.38), Inches(0.42), font_size=13, bold=True,
                 color=RGBColor(255, 255, 255), align=PP_ALIGN.CENTER,
                 font_name="Calibri")

    return slide
```

## 範例

### 輸入範例
「第3章節分隔：{subsidiary_name_cn}主要業務（第三章 THREE）」

### 輸出效果
淺灰全頁背景，左側深海軍藍大方塊顯示「P / ART 03」，
左下方空心輪廓方塊裝飾，右側「{subsidiary_name_cn}主要業務」34pt 粗體 + 藍色底線，
右下角「THREE」白字藍底徽章
