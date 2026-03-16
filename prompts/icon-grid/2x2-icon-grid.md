---
layout: icon_grid
name: 圖示網格（2×2 田字型）
tags: [icon-grid, 2x2, grid, features, overview]
---

# 圖示網格 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│  整體標題文字  28pt Bold                                     │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│  ┌──────────────────────┬──────────────────────┐            │
│  │      ╭───╮           │      ╭───╮           │            │
│  │      │ ① │           │      │ ② │           │            │
│  │      ╰───╯           │      ╰───╯           │            │
│  │   格子標題 A         │   格子標題 B         │            │
│  │   說明說明說明說明   │   說明說明說明說明   │            │
│  │   說明說明           │   說明說明           │            │
│  ├──────────────────────┼──────────────────────┤            │
│  │      ╭───╮           │      ╭───╮           │            │
│  │      │ ③ │           │      │ ④ │           │            │
│  │      ╰───╯           │      ╰───╯           │            │
│  │   格子標題 C         │   格子標題 D         │            │
│  │   說明說明說明說明   │   說明說明說明說明   │            │
│  │   說明說明           │   說明說明           │            │
│  └──────────────────────┴──────────────────────┘            │
│  ─────────────────────────────────────────────────────────  │
└─────────────────────────────────────────────────────────────┘
```

## 適用情境

- 功能特色一覽：以四格呈現產品的四大核心功能
- 服務項目展示：並列四種服務類型及其簡介
- 特性比較總覽：展示四個面向的差異化優勢

## Core Prompt

```
Generate an icon grid slide (16:9, 13.33" × 7.50"):

=== TITLE AREA ===
Title text: "{slide_title}" — 28pt, Bold, {title_color}
  Position: x=0.50", y=0.30", width=12.30", height=0.60"
Title underline:
  Rectangle: x=0.50", y=1.00", width=12.30", height=0.04"
  Fill: {accent_color}

=== GRID LAYOUT ===
Grid mode: {grid_mode} — "2x2" (4 cells) or "3x2" (6 cells)
Grid outer boundary: x=0.50", y=1.15", width=12.30", height=5.90"

For 2×2 grid:
  Cell width  = 6.15"
  Cell height = 2.95"
  Columns: x=0.50", x=6.65"
  Rows:    y=1.15", y=4.10"

For 3×2 grid:
  Cell width  = 4.10"
  Cell height = 2.95"
  Columns: x=0.50", x=4.60", x=8.70"
  Rows:    y=1.15", y=4.10"

=== GRID DIVIDERS ===
Vertical divider(s):
  Rectangle: x=col_boundary, y=1.15", width=0.02", height=5.90"
  Fill: {divider_color}

Horizontal divider:
  Rectangle: x=0.50", y=4.08", width=12.30", height=0.02"
  Fill: {divider_color}

Outer border (optional):
  Rectangle: x=0.50", y=1.15", width=12.30", height=5.90"
  Fill: none, border: {divider_color} (0.5pt)

=== CELL CONTENT ===
For each cell {c} (left-to-right, top-to-bottom):
  Cell origin: (cell_x, cell_y)

  Icon placeholder:
    Shape: circle (or square)
    x = cell_x + cell_w/2 - 0.38", y = cell_y + 0.25"
    width=0.76", height=0.76"
    Fill: {icon_bg_color}
    (Represents the icon area — replace with actual icon in production)

  Icon label (inside placeholder, optional):
    Text: "{icon_label_c}" — 14pt, Bold, white
    Centered within icon placeholder

  Cell title:
    Text: "{cell_title_c}" — 15pt, Bold, {cell_title_color}
    Position: x=cell_x+0.25", y=cell_y+1.10", width=cell_w-0.50", height=0.44"
    Align: center (or left if preferred)

  Cell description:
    Text: "{cell_desc_c}" — 11pt, normal, {cell_desc_color}
    Position: x=cell_x+0.25", y=cell_y+1.60", width=cell_w-0.50", height=1.20"
    Align: center (or left), word wrap enabled

=== BOTTOM DECORATION ===
Thin rectangle: x=0.50", y=7.18", width=12.30", height=0.05"
Fill: {bottom_line_color}

Content to fill in:
Grid mode: {grid_mode}
{cells_content}
  Format:
  Cell 1: icon_label="{icon_label_1}", title="{cell_title_1}", desc="{cell_desc_1}"
  Cell 2: icon_label="{icon_label_2}", title="{cell_title_2}", desc="{cell_desc_2}"
  Cell 3: icon_label="{icon_label_3}", title="{cell_title_3}", desc="{cell_desc_3}"
  Cell 4: icon_label="{icon_label_4}", title="{cell_title_4}", desc="{cell_desc_4}"
  (Cell 5–6 for 3×2 mode only)
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 投影片整體標題 | `四大核心服務` |
| `{title_color}` | 主標題文字色 | `#404040` |
| `{accent_color}` | 標題底線色 | `#0091D5` |
| `{grid_mode}` | 格子模式 | `2x2` 或 `3x2` |
| `{icon_bg_color}` | 圖示佔位符背景色（品牌色） | `#0091D5` |
| `{icon_label_c}` | 第 c 格圖示佔位符標籤（簡短） | `海運` |
| `{cell_title_c}` | 第 c 格標題 | `海運進出口` |
| `{cell_title_color}` | 格子標題文字色 | `#1B4F9B` |
| `{cell_desc_c}` | 第 c 格說明文字（2–3 行） | `提供 FCL 整櫃與 LCL 併櫃服務，涵蓋全球主要航線` |
| `{cell_desc_color}` | 格子說明文字色 | `#555555` |
| `{divider_color}` | 格線顏色 | `#DDDDDD` |
| `{bottom_line_color}` | 底部裝飾線色（極淺） | `#E8F4FD` |
| `{brand_name}` | 品牌名稱 | `（替換為實際品牌名）` |

## python-pptx 程式碼骨架

```python
def build_icon_grid(slide, s: dict):
    """
    建立圖示網格（2×2 或 3×2）版型

    Args:
        slide: 空白投影片物件
        s: dict，包含以下欄位：
            slide_title (str): 投影片標題
            grid_mode (str): "2x2" 或 "3x2"，預設 "2x2"
            cells (list): 格子資料列表，每項為
                {"icon_label": str, "title": str, "desc": str}
            icon_bg_color (tuple): 圖示佔位符背景 RGB，預設 (0, 145, 213)
            accent_color (tuple): 主強調色 RGB，預設 (0, 145, 213)
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    accent = RGBColor(*s.get("accent_color", (0, 145, 213)))
    icon_bg = RGBColor(*s.get("icon_bg_color", (0, 145, 213)))
    dark = RGBColor(64, 64, 64)
    navy = RGBColor(27, 79, 155)
    mid = RGBColor(85, 85, 85)
    white = RGBColor(255, 255, 255)
    divider = RGBColor(0xDD, 0xDD, 0xDD)
    bottom_line = RGBColor(0xE8, 0xF4, 0xFD)

    # — 標題 —
    add_text(slide, s["slide_title"],
             Inches(0.50), Inches(0.30), Inches(12.30), Inches(0.60),
             font_size=28, bold=True, color=dark, align="left", font_name="Calibri")
    add_rect(slide, Inches(0.50), Inches(1.00), Inches(12.30), Inches(0.04),
             fill_color=accent)

    mode = s.get("grid_mode", "2x2")
    cells = s.get("cells", [])

    if mode == "3x2":
        cols = 3
        cell_w = 4.10
        col_xs = [0.50, 4.60, 8.70]
        max_cells = 6
    else:
        cols = 2
        cell_w = 6.15
        col_xs = [0.50, 6.65]
        max_cells = 4

    rows = 2
    cell_h = 2.95
    row_ys = [1.15, 4.10]

    # 外框
    add_rect(slide, Inches(0.50), Inches(1.15), Inches(12.30), Inches(5.90),
             fill_color=None, border_color=divider)

    # 水平分隔線
    add_rect(slide, Inches(0.50), Inches(4.08), Inches(12.30), Inches(0.02),
             fill_color=divider)

    # 垂直分隔線
    for ci in range(1, cols):
        vx = col_xs[ci] - 0.02
        add_rect(slide, Inches(vx), Inches(1.15), Inches(0.02), Inches(5.90),
                 fill_color=divider)

    # 格子內容
    for idx, cell in enumerate(cells[:max_cells]):
        row = idx // cols
        col = idx % cols
        cx = col_xs[col]
        cy = row_ys[row]

        # 圖示佔位符
        icon_x = cx + cell_w / 2 - 0.38
        add_rect(slide, Inches(icon_x), Inches(cy + 0.25),
                 Inches(0.76), Inches(0.76), fill_color=icon_bg)
        if cell.get("icon_label"):
            add_text(slide, cell["icon_label"],
                     Inches(icon_x), Inches(cy + 0.39),
                     Inches(0.76), Inches(0.48),
                     font_size=13, bold=True, color=white, align="center", font_name="Calibri")

        # 格子標題
        add_text(slide, cell.get("title", ""),
                 Inches(cx + 0.25), Inches(cy + 1.10),
                 Inches(cell_w - 0.50), Inches(0.44),
                 font_size=15, bold=True, color=navy, align="center", font_name="Calibri")

        # 格子說明
        add_text(slide, cell.get("desc", ""),
                 Inches(cx + 0.25), Inches(cy + 1.60),
                 Inches(cell_w - 0.50), Inches(1.20),
                 font_size=11, bold=False, color=mid, align="center", font_name="Calibri")

    # — 底部裝飾線 —
    add_rect(slide, Inches(0.50), Inches(7.18), Inches(12.30), Inches(0.05),
             fill_color=bottom_line)
```

## 範例

### 輸入範例

```
標題：{brand_name} 四大核心服務

grid_mode: "2x2"

Cell 1: icon_label="海運", title="海運進出口",
  desc="提供 FCL 整櫃與 LCL 併櫃服務，涵蓋全球主要航線，門到門全程掌控"

Cell 2: icon_label="空運", title="空運快遞",
  desc="時效性高價值貨物首選，與主要航空公司深度合作，確保準時交付"

Cell 3: icon_label="倉儲", title="倉儲物流",
  desc="智慧化倉庫管理系統，即時庫存查詢，支援電商出貨與逆物流"

Cell 4: icon_label="報關", title="報關代理",
  desc="AEO 安全認證企業，優先快速通關，全面 EDI 電子資料交換"
```

### 輸出效果

白底，藍色粗體標題與底線，四格等寬等高的田字型網格，
格線以淺灰色細線分隔，每格頂部有品牌藍色圓形圖示佔位符（含簡短標籤），
格內有深藍粗體標題與多行說明文字，
底部淺藍極細裝飾線收尾。
