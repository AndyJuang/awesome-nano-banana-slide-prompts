---
layout: contents
name: 深色左欄數字徽章目錄
tags: [toc, contents, numbered-badge, dark-panel]
source: 曜捷_公司簡介_簡報草稿_20260310.pptx — Slide 2
---

# 深色左欄數字徽章目錄 Prompt 模版

> 精確尺寸來源：實際 PPTX 解析（13.33" × 7.5"，16:9）

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│ ┌────────────────────┐  ┌──────────────────────────────────┐ │
│ │  ■ (0.35,2.7)      │  │  ┌────┐  章節標題  16pt Bold     │ │
│ │  ● (0.75,2.9)      │  │  │ 1  │  英文副標題  10pt        │ │
│ │                    │  │  └────┘  ─────────────────────  │ │
│ │  目錄  34pt Bold   │  │  ┌────┐  章節標題                │ │
│ │  contents 20pt     │  │  │ 2  │  英文副標題              │ │
│ │                    │  │  └────┘  ─────────────────────  │ │
│ │  深色左欄 #2D415F   │  │  ...（最多 6 項）                │ │
│ │  5.8" × 7.5"       │  │                                  │ │
│ └────────────────────┘  └──────────────────────────────────┘ │
│                                          [Logo 右下 9pt]     │
└─────────────────────────────────────────────────────────────┘
```

## 版面精確規格

```
Slide: 13.33" × 7.50"

── 左欄（5.8" 寬，全高）──
Dark Panel:      left=0.00"  top=0.00"  w=5.80"  h=7.50"  fill=#2D415F
Deco Square 1:   left=0.35"  top=2.70"  w=0.32"  h=0.32"  fill=#1B4F9B
Deco Square 2:   left=0.75"  top=2.90"  w=0.22"  h=0.22"  fill=#0091D5
Label CN:        left=0.50"  top=2.85"  w=4.50"  h=0.85"  34pt Bold white
Label EN:        left=0.50"  top=3.65"  w=4.50"  h=0.60"  20pt Bold white

── 右欄目錄項目（從 x=6.10" 開始，重複 N 次）──
每個目錄項目高度 ≈ 1.12"，第一項 y=0.35"

Per-item template (item index i, y_start = 0.35 + i × 1.12):
  Badge:       left=6.10"  top=y_start  w=0.58"  h=0.58"
               fill = #1B4F9B (奇數項) | #808080 (偶數項)
  Number text: left=6.10"  top=y_start+0.08  w=0.58"  h=0.45"  18pt Bold white center
  Title CN:    left=6.90"  top=y_start  w=6.00"  h=0.38"  16pt Bold #404040
  Title EN:    left=6.90"  top=y_start+0.37  w=6.00"  h=0.26"  10pt normal #808080
  Separator:   left=6.10"  top=y_start+0.68  w=6.80"  h=0.025"  fill=#F0F0F0

── 右下角 Logo ──
Logo Text:     left=11.30"  top=7.10"  w=1.90"  h=0.32"  9pt Bold brand color
```

## Core Prompt

```
Generate a table of contents slide (16:9, 13.33" × 7.50"):

=== LEFT PANEL (dark sidebar) ===
Rectangle:
  Position: x=0, y=0, width=5.80", height=7.50" (full height)
  Fill: dark slate {panel_color}

Decorative elements on left panel:
  Square 1: x=0.35", y=2.70", size=0.32"×0.32", fill={accent_color_1}
  Square 2: x=0.75", y=2.90", size=0.22"×0.22", fill={accent_color_2}

Panel label:
  Primary text: "{label_primary}" — 34pt, Bold, white
    Position: x=0.50", y=2.85", width=4.50"
  Secondary text: "{label_secondary}" — 20pt, Bold, white
    Position: x=0.50", y=3.65", width=4.50"

=== RIGHT PANEL (contents list) ===
Starting x=6.10", first item y=0.35"
Item vertical spacing: 1.12" per item
Maximum items: 6

For each item {i} (i = 1 to N, y = 0.35 + (i-1) × 1.12"):

  Numbered badge:
    Rectangle: x=6.10", y=y_start, width=0.58", height=0.58"
    Fill: {badge_color_odd} for odd items, {badge_color_even} for even items
    Number text: "{i}" — 18pt, Bold, white, centered

  Item title (primary language):
    Text: "{item_title_i}" — 16pt, Bold, {title_color}
    Position: x=6.90", y=y_start, width=6.00", height=0.38"

  Item subtitle (secondary language):
    Text: "{item_subtitle_i}" — 10pt, normal, {subtitle_color}
    Position: x=6.90", y=y_start+0.37", width=6.00", height=0.26"

  Separator line:
    Rectangle: x=6.10", y=y_start+0.68", width=6.80", height=0.025"
    Fill: {separator_color}

=== LOGO (bottom right) ===
Text: "{logo_text}" — 9pt, Bold, {logo_color}
Position: x=11.30", y=7.10", width=1.90"

Items to include:
{items_list}
  Format:
  - Item 1: title="{title}", subtitle="{subtitle}"
  - Item 2: ...
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{panel_color}` | 左側深色欄背景色 | `#2D415F` |
| `{accent_color_1}` | 裝飾方塊1顏色 | `#1B4F9B` |
| `{accent_color_2}` | 裝飾方塊2顏色 | `#0091D5` |
| `{label_primary}` | 左欄大字標籤（中文） | `目錄` |
| `{label_secondary}` | 左欄小字標籤（英文） | `contents` |
| `{badge_color_odd}` | 奇數項數字徽章色 | `#1B4F9B`（品牌深藍）|
| `{badge_color_even}` | 偶數項數字徽章色 | `#808080`（中灰）|
| `{title_color}` | 章節標題文字色 | `#404040` |
| `{subtitle_color}` | 英文副標題色 | `#808080` |
| `{separator_color}` | 分隔線顏色 | `#F0F0F0` |
| `{logo_text}` | 右下角 Logo | `BRAND NAME` |
| `{logo_color}` | Logo 文字色 | `#1B4F9B` |
| `{items_list}` | 目錄項目（最多6項） | 見範例 |
| `{group_name}` | 集團英文簡稱（用於目錄章節標題） | `{group_name}` |

## python-pptx 程式碼骨架

```python
def build_dark_panel_toc(prs, label_primary, label_secondary, items,
                          panel_color=None, badge_colors=None, logo_text="BRAND"):
    """
    建立深色左欄數字徽章目錄

    Args:
        label_primary: 左欄主標籤（如「目錄」）
        label_secondary: 左欄副標籤（如「contents」）
        items: list of {"title": str, "subtitle": str}，最多6項
        panel_color: 左欄背景色，預設 #2D415F
        badge_colors: (odd_color, even_color)，預設 (#1B4F9B, #808080)
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN

    slide = prs.slides.add_slide(prs.slide_layouts[6])

    if panel_color is None:
        panel_color = RGBColor(0x2D, 0x41, 0x5F)
    if badge_colors is None:
        badge_colors = (RGBColor(0x1B, 0x4F, 0x9B), RGBColor(0x80, 0x80, 0x80))

    # 左側深色欄
    add_rect(slide, 0, 0, Inches(5.80), prs.slide_height,
             fill_color=panel_color)

    # 左欄裝飾方塊
    add_rect(slide, Inches(0.35), Inches(2.70), Inches(0.32), Inches(0.32),
             fill_color=RGBColor(0x1B, 0x4F, 0x9B))
    add_rect(slide, Inches(0.75), Inches(2.90), Inches(0.22), Inches(0.22),
             fill_color=RGBColor(0x00, 0x91, 0xD5))

    # 左欄標籤
    add_text_box(slide, label_primary, Inches(0.50), Inches(2.85),
                 Inches(4.50), Inches(0.85), font_size=34, bold=True,
                 color=RGBColor(255, 255, 255))
    add_text_box(slide, label_secondary, Inches(0.50), Inches(3.65),
                 Inches(4.50), Inches(0.60), font_size=20, bold=True,
                 color=RGBColor(255, 255, 255), font_name="Calibri")

    # 目錄項目
    ITEM_X = Inches(6.10)
    ITEM_SPACING = Inches(1.12)
    FIRST_Y = Inches(0.35)
    BADGE_W = Inches(0.58)

    for i, item in enumerate(items[:6]):
        y = FIRST_Y + ITEM_SPACING * i
        badge_color = badge_colors[0] if i % 2 == 0 else badge_colors[1]

        # 數字徽章
        add_rect(slide, ITEM_X, y, BADGE_W, BADGE_W, fill_color=badge_color)
        add_text_box(slide, str(i + 1), ITEM_X, y + Inches(0.08),
                     BADGE_W, Inches(0.45), font_size=18, bold=True,
                     color=RGBColor(255, 255, 255), align=PP_ALIGN.CENTER,
                     font_name="Calibri")

        # 中文標題
        add_text_box(slide, item["title"],
                     ITEM_X + BADGE_W + Inches(0.22), y,
                     Inches(6.00), Inches(0.38),
                     font_size=16, bold=True, color=RGBColor(64, 64, 64))

        # 英文副標題
        if item.get("subtitle"):
            add_text_box(slide, item["subtitle"],
                         ITEM_X + BADGE_W + Inches(0.22), y + Inches(0.37),
                         Inches(6.00), Inches(0.26),
                         font_size=10, color=RGBColor(128, 128, 128),
                         font_name="Calibri")

        # 分隔線
        add_rect(slide, ITEM_X, y + Inches(0.68),
                 Inches(6.80), Inches(0.025),
                 fill_color=RGBColor(240, 240, 240))

    # 右下角 Logo
    add_text_box(slide, logo_text, Inches(11.30), Inches(7.10),
                 Inches(1.90), Inches(0.32), font_size=9, bold=True,
                 color=RGBColor(0x1B, 0x4F, 0x9B), font_name="Calibri")

    return slide
```

## 範例

### 輸入範例
6 個章節：「集團背景概覽 / {group_name} OVERVIEW」、「公司簡介 / INTRODUCTION」、
「主要業務 / SERVICES」、「合作夥伴 / PARTNERS」、「服務網絡 / NETWORK」、「聯絡資訊 / CONTACT」

### 輸出效果
左側 5.8" 深板岩藍全高欄，中央「目錄 / contents」白色大字，
右側 6 行數字徽章（奇數深藍、偶數灰），每項含中英文標題，灰色細線分隔
