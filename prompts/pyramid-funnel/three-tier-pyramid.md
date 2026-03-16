---
layout: pyramid_funnel
name: 三層金字塔 / 漏斗圖
tags: [pyramid, funnel, three-tier, hierarchy, priority]
---

# 三層金字塔 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│  標題文字  28pt Bold                                         │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│              ┌──────────────┐                               │
│              │   第一層     │◀ 層一標題  說明文字            │
│          ┌───┴──────────────┴───┐                           │
│          │      第二層          │◀ 層二標題  說明文字        │
│      ┌───┴──────────────────────┴───┐                       │
│      │           第三層             │◀ 層三標題  說明文字   │
│      └─────────────────────────────┘                       │
│                                                              │
│  ─────────────────────────────────────────────────────────  │
└─────────────────────────────────────────────────────────────┘
```

## 適用情境

- 優先順序分層：將策略目標依重要性排列為三個層級
- 市場分級：按客戶規模或價值分層展示目標市場
- 層次架構展示：如「願景 → 目標 → 行動」三層策略結構

## Core Prompt

```
Generate a three-tier pyramid (or funnel) diagram slide (16:9, 13.33" × 7.50"):

=== TITLE AREA ===
Title text: "{slide_title}" — 28pt, Bold, {title_color}
  Position: x=0.50", y=0.30", width=12.30", height=0.60"
Title underline:
  Rectangle: x=0.50", y=1.00", width=12.30", height=0.04"
  Fill: {accent_color}

=== PYRAMID / FUNNEL SHAPE ===
Mode: {diagram_mode} — "pyramid" (top narrow) or "funnel" (top wide)
Label side: {label_side} — "left" or "right"

Pyramid layout (diagram_mode = "pyramid"):
  Layer 1 (top, narrowest):
    Trapezoid width: 2.60"
    x = center_x - 1.30" = 5.37"
    y = 1.40", height = 1.40"
    Fill: {color_tier1}

  Layer 2 (middle):
    Trapezoid width: 5.20"
    x = center_x - 2.60" = 4.07"
    y = 2.80", height = 1.40"
    Fill: {color_tier2}

  Layer 3 (bottom, widest):
    Trapezoid width: 7.80"
    x = center_x - 3.90" = 2.77"
    y = 4.20", height = 1.40"
    Fill: {color_tier3}

  (Each layer is a rectangle. For true trapezoid effect, use PowerPoint's isoceles
   triangle shape clipped or use freeform shapes. As a simplification, use
   rectangles with increasing width for a staircase pyramid look.)

Funnel layout (diagram_mode = "funnel"): reverse the widths top-to-bottom.
  Layer 1 (top, widest):  width=7.80", x=2.77"
  Layer 2 (middle):       width=5.20", x=4.07"
  Layer 3 (bottom, narrowest): width=2.60", x=5.37"
  y positions same: 1.40", 2.80", 4.20"

=== LAYER CONTENT ===
For each layer {t} (t=1, 2, 3):
  Layer title (inside the shape):
    Text: "{tier_title_t}" — 16pt, Bold, white
    Position: centered vertically in layer rectangle, full width of rectangle
    Align: center

  Layer label (outside, on {label_side}):
    If label_side = "right":
      x = shape_right + 0.20"
    If label_side = "left":
      x = shape_left - 3.00"
    y = layer_top + 0.45"

    Label title: "{tier_label_t}" — 14pt, Bold, {label_title_color}
      width=2.60", height=0.36"
    Label desc: "{tier_desc_t}" — 11pt, normal, {label_desc_color}
      Position: x=same, y=label_y+0.38", width=2.60", height=0.56"

    Connector line (from label to layer edge):
      Thin rectangle: from shape edge to label text
      width=0.18", height=0.04", Fill: {connector_color}

=== BOTTOM DECORATION ===
Thin rectangle: x=0.50", y=7.18", width=12.30", height=0.05"
Fill: {bottom_line_color}

Content to fill in:
Mode: {diagram_mode}
Label side: {label_side}
Tier 1: title="{tier_title_1}", label="{tier_label_1}", desc="{tier_desc_1}", color={color_tier1}
Tier 2: title="{tier_title_2}", label="{tier_label_2}", desc="{tier_desc_2}", color={color_tier2}
Tier 3: title="{tier_title_3}", label="{tier_label_3}", desc="{tier_desc_3}", color={color_tier3}
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 投影片主標題 | `策略優先順序框架` |
| `{title_color}` | 主標題文字色 | `#404040` |
| `{accent_color}` | 標題底線色 | `#0091D5` |
| `{diagram_mode}` | 圖型模式 | `pyramid`（頂層窄）或 `funnel`（頂層寬）|
| `{label_side}` | 標籤位置 | `right` 或 `left` |
| `{color_tier1}` | 第一層填色 | `#1B4F9B`（深藍） |
| `{color_tier2}` | 第二層填色 | `#0091D5`（中藍） |
| `{color_tier3}` | 第三層填色 | `#5BB8E8`（淺藍） |
| `{tier_title_t}` | 第 t 層內部標題文字 | `願景` |
| `{tier_label_t}` | 第 t 層外部標籤標題 | `願景層` |
| `{tier_desc_t}` | 第 t 層外部說明文字 | `成為亞洲最值得信賴的物流夥伴` |
| `{label_title_color}` | 外部標籤標題文字色 | `#1B4F9B` |
| `{label_desc_color}` | 外部標籤說明文字色 | `#555555` |
| `{connector_color}` | 連接線顏色 | `#AACCE8` |
| `{bottom_line_color}` | 底部裝飾線色（極淺） | `#E8F4FD` |
| `{brand_name}` | 品牌名稱 | `（替換為實際品牌名）` |

## python-pptx 程式碼骨架

```python
def build_pyramid_funnel(slide, s: dict):
    """
    建立三層金字塔 / 漏斗圖版型

    Args:
        slide: 空白投影片物件
        s: dict，包含以下欄位：
            slide_title (str): 投影片標題
            diagram_mode (str): "pyramid" 或 "funnel"，預設 "pyramid"
            label_side (str): "right" 或 "left"，預設 "right"
            tiers (list): 三層資料，每項為
                {"title": str, "label": str, "desc": str, "color": tuple}
            accent_color (tuple): 主強調色 RGB，預設 (0, 145, 213)
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    accent = RGBColor(*s.get("accent_color", (0, 145, 213)))
    dark = RGBColor(64, 64, 64)
    navy = RGBColor(27, 79, 155)
    mid = RGBColor(85, 85, 85)
    white = RGBColor(255, 255, 255)
    connector_color = RGBColor(0xAA, 0xCC, 0xE8)
    bottom_line = RGBColor(0xE8, 0xF4, 0xFD)

    # — 標題 —
    add_text(slide, s["slide_title"],
             Inches(0.50), Inches(0.30), Inches(12.30), Inches(0.60),
             font_size=28, bold=True, color=dark, align="left", font_name="Calibri")
    add_rect(slide, Inches(0.50), Inches(1.00), Inches(12.30), Inches(0.04),
             fill_color=accent)

    mode = s.get("diagram_mode", "pyramid")
    label_side = s.get("label_side", "right")
    tiers = s.get("tiers", [])[:3]
    if len(tiers) < 3:
        return

    center_x = 6.67
    layer_h = 1.40
    y_starts = [1.40, 2.80, 4.20]

    # 金字塔模式：層序 0=頂（最窄），2=底（最寬）
    # 漏斗模式：層序 0=頂（最寬），2=底（最窄）
    widths_pyramid = [2.60, 5.20, 7.80]
    widths_funnel = [7.80, 5.20, 2.60]
    widths = widths_pyramid if mode == "pyramid" else widths_funnel

    default_colors = [
        RGBColor(27, 79, 155),
        RGBColor(0, 145, 213),
        RGBColor(91, 184, 232),
    ]

    for i, tier in enumerate(tiers):
        w = widths[i]
        x = center_x - w / 2
        y = y_starts[i]
        color = RGBColor(*tier["color"]) if "color" in tier else default_colors[i]

        # 層矩形
        add_rect(slide, Inches(x), Inches(y), Inches(w), Inches(layer_h),
                 fill_color=color)

        # 層內標題
        add_text(slide, tier.get("title", ""),
                 Inches(x), Inches(y + 0.48),
                 Inches(w), Inches(0.44),
                 font_size=16, bold=True, color=white, align="center", font_name="Calibri")

        # 外部標籤
        if label_side == "right":
            label_x = x + w + 0.20
            connector_x = x + w
        else:
            label_x = x - 2.80
            connector_x = label_x + 2.80

        label_y = y + 0.45

        # 連接線
        add_rect(slide, Inches(connector_x), Inches(label_y + 0.14),
                 Inches(0.18), Inches(0.04), fill_color=connector_color)

        # 標籤標題
        add_text(slide, tier.get("label", tier.get("title", "")),
                 Inches(label_x), Inches(label_y),
                 Inches(2.60), Inches(0.36),
                 font_size=14, bold=True, color=navy, align="left", font_name="Calibri")

        # 標籤說明
        add_text(slide, tier.get("desc", ""),
                 Inches(label_x), Inches(label_y + 0.38),
                 Inches(2.60), Inches(0.56),
                 font_size=11, bold=False, color=mid, align="left", font_name="Calibri")

    # — 底部裝飾線 —
    add_rect(slide, Inches(0.50), Inches(7.18), Inches(12.30), Inches(0.05),
             fill_color=bottom_line)
```

## 範例

### 輸入範例

```
標題：{brand_name} 三年策略優先順序

diagram_mode: "pyramid"
label_side: "right"

Tier 1（頂層）：
  title="願景", label="願景層", desc="成為亞洲最值得信賴的物流夥伴"
  color=(27, 79, 155)

Tier 2（中層）：
  title="目標", label="目標層", desc="2027 年營收倍增，客戶滿意度達 95%"
  color=(0, 145, 213)

Tier 3（底層）：
  title="行動", label="行動層", desc="數位轉型、拓展航線、強化人才培育"
  color=(91, 184, 232)
```

### 輸出效果

白底，藍色粗體標題與底線，版面中央三個由上至下漸寬的矩形模擬金字塔，
頂層深藍顯示「願景」，中層品牌藍顯示「目標」，底層淺藍顯示「行動」，
每層右側有連接線引出標籤標題與說明文字，
底部淺藍極細裝飾線收尾。
