---
layout: table
name: 基礎表格頁
tags: [table, data, comparison, specs]
---

# 基礎表格頁 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO]                                    ■ ■ □            │
│  ■ 標題文字                                                   │
│  ────────────────────────────                               │
│                                                              │
│  ┌──────────────┬─────────────────────────────────────────┐ │
│  │  欄位標題 1  │  欄位標題 2   │  欄位標題 3  │ 欄位標題 4 │ │
│  ├──────────────┼──────────────┼──────────────┼────────────┤ │
│  │  列標籤      │  資料內容     │   資料內容   │  資料內容  │ │
│  ├──────────────┼──────────────┼──────────────┼────────────┤ │
│  │  列標籤      │  資料內容     │   資料內容   │  資料內容  │ │
│  ├──────────────┼──────────────┼──────────────┼────────────┤ │
│  │  列標籤      │  資料內容     │ ★ 強調數值   │  資料內容  │ │
│  └──────────────┴──────────────┴──────────────┴────────────┘ │
│  * 附註文字（可選）                                            │
└─────────────────────────────────────────────────────────────┘
```

## 適用場景

- 規格比較表（產品/方案/報價）
- 資料彙整（KPI 表、時程表）
- 標籤-說明對照（服務項目清單）

## Core Prompt

```
Generate a table slide (16:9):

Title: "{title}" with small accent marker at left

Table specifications:
  Dimensions: {rows} data rows + 1 header row, {cols} columns
  Table width: {table_width}% of slide width, horizontally {table_align}
  Table top position: {table_top}% from slide top

Header row:
  Background: {header_bg_color}
  Text color: {header_text_color}
  Text style: bold, {header_font_size}pt, centered
  Column headers (left to right): [{col_headers}]
  Column width ratios: [{col_width_ratios}]
    e.g., [20, 30, 25, 25] — must sum to 100

Data rows:
  Alternating row colors:
    Odd rows: {odd_row_color}
    Even rows: {even_row_color}
  Row height: {row_height}px or "auto"
  Text alignment per column: [{col_alignments}]
    Options per column: "left" | "center" | "right"
  Text style: {data_font_size}pt, normal weight

Row data (provide as structured list):
{row_data}
  Format: Row N: [cell1, cell2, ...]
  Special: wrap highlighted cells in **double asterisks** to apply emphasis color

Emphasis cells:
  Color: {emphasis_color}
  Style: bold

Left column (label column) style:
  {left_col_style}
  Options: "same as other data" | "bold with accent color" | "dark background white text"

Footer / footnote:
  "{footnote}" (leave empty if none)
  Position: below table, small muted text

Color palette:
  Header background: {header_bg_color}
  Header text: {header_text_color}
  Odd rows: {odd_row_color}
  Even rows: {even_row_color}
  Emphasis: {emphasis_color}
  Border: {border_color} at {border_width}px
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{title}` | 投影片標題 | `服務方案比較` |
| `{rows}` | 資料列數（不含表頭） | `5` |
| `{cols}` | 欄位數 | `4` |
| `{table_width}` | 表格佔投影片寬度 % | `90` |
| `{table_align}` | 表格水平對齊 | `centered` |
| `{table_top}` | 表格距頂部 % | `22` |
| `{header_bg_color}` | 表頭背景色 | `#0091D5` 或 `brand blue` |
| `{header_text_color}` | 表頭文字色 | `white` |
| `{header_font_size}` | 表頭字號 | `16` |
| `{col_headers}` | 欄位標題陣列 | `"項目", "基本版", "專業版", "企業版"` |
| `{col_width_ratios}` | 各欄位寬度比例 | `[25, 25, 25, 25]` |
| `{odd_row_color}` | 奇數列底色 | `white` 或 `#FFFFFF` |
| `{even_row_color}` | 偶數列底色 | `#E8F4FD` (淺藍) |
| `{row_height}` | 列高 | `40` 或 `auto` |
| `{col_alignments}` | 各欄對齊方式 | `["left", "center", "center", "center"]` |
| `{data_font_size}` | 資料字號 | `14` |
| `{emphasis_color}` | 強調格顏色 | `#0091D5` |
| `{left_col_style}` | 左欄（標籤欄）樣式 | `bold with accent color` |
| `{footnote}` | 表格下方附註 | `* 價格不含稅，以實際報價為準` |
| `{border_color}` | 表格邊框色 | `#C8C8C8` |
| `{border_width}` | 邊框粗細 | `1` |
| `{row_data}` | 各列資料（含強調標記） | `Row 1: ["倉儲服務", "✓", "✓", "✓"]` |

## 版型細節規範

### 版面配置
- 標題距頂：5–8%
- 表格距標題：3–5%
- 表格距底：5–8%
- 最佳列數：4–8 列（超過請考慮截頁或縮小字號）

### 欄位設計原則
- 第一欄通常為「標籤欄」（較窄，加粗/深色）
- 數字欄位右對齊
- 文字欄位左對齊
- 勾選/狀態欄置中

### 強調設計
- 用色塊或粗體突顯關鍵數字
- 表頭與資料區對比要夠強（亮度差 > 40%）
- 避免超過 2 種強調色

## python-pptx 程式碼骨架

```python
def build_table_slide(prs, title, col_headers, rows_data,
                      accent_color, light_row_color=None):
    """
    建立表格投影片

    Args:
        prs: Presentation 物件
        title: 標題文字 (str)
        col_headers: 欄位標題清單 (list[str])
        rows_data: 資料列清單 (list[list[str]])
        accent_color: RGBColor，表頭背景色
        light_row_color: RGBColor，偶數列底色，預設淺藍
    """
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    W, H = prs.slide_width, prs.slide_height

    if light_row_color is None:
        light_row_color = RGBColor(232, 244, 253)

    PADDING = Inches(0.4)

    # 標題
    add_rect(slide, PADDING, Inches(0.45), Inches(0.12), Inches(0.5),
             fill_color=accent_color)
    add_text_box(slide, title, PADDING + Inches(0.2), Inches(0.4),
                 W - PADDING * 2, Inches(0.6),
                 font_size=22, bold=True, color=RGBColor(40, 40, 40))

    # 表格
    num_cols = len(col_headers)
    num_rows = len(rows_data) + 1  # +1 for header

    tbl_left = PADDING
    tbl_top = Inches(1.3)
    tbl_width = W - PADDING * 2
    tbl_height = H - tbl_top - Inches(0.5)

    table = slide.shapes.add_table(
        num_rows, num_cols, tbl_left, tbl_top, tbl_width, tbl_height
    ).table

    # 表頭列
    for col_idx, header in enumerate(col_headers):
        cell = table.cell(0, col_idx)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = accent_color
        para = cell.text_frame.paragraphs[0]
        para.alignment = PP_ALIGN.CENTER
        run = para.runs[0]
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.size = Pt(14)

    # 資料列
    for row_idx, row_data in enumerate(rows_data):
        bg = light_row_color if row_idx % 2 == 1 else RGBColor(255, 255, 255)
        for col_idx, cell_text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = str(cell_text)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            para = cell.text_frame.paragraphs[0]
            para.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT
            run = para.runs[0] if para.runs else para.add_run()
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(64, 64, 64)

    return slide
```

## 範例

### 輸入範例
「比較三種服務方案（基本/專業/企業），項目包含：倉儲空間、配送次數、客服支援、系統整合、價格」

### 輸出效果
藍色表頭帶白字，5 列資料交替白/淺藍底色，
第一欄（項目名）藍色粗體，企業版欄位強調標示最高配額
