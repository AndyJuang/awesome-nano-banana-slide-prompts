---
layout: three_columns
name: 三欄支柱 / 三大亮點
tags: [three-columns, pillars, highlights, checklist, comparison]
---

# 三欄支柱 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│  整體標題文字  28pt Bold                                     │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│  ┌──────────────┬══════════════╗──────────────┐             │
│  │   ╭───╮      ║   ╭───╮     ║   ╭───╮      │             │
│  │   │ A │      ║   │ B │     ║   │ C │      │             │
│  │   ╰───╯      ║   ╰───╯     ║   ╰───╯      │             │
│  │  欄位標題一  ║  欄位標題二 ║  欄位標題三  │             │
│  │              ║             ║              │             │
│  │  ✓ 重點一    ║  ✓ 重點一   ║  ✓ 重點一    │             │
│  │  ✓ 重點二    ║  ✓ 重點二   ║  ✓ 重點二    │             │
│  │  ✓ 重點三    ║  ✓ 重點三   ║  ✓ 重點三    │             │
│  │  ✓ 重點四    ║  ✓ 重點四   ║  ✓ 重點四    │             │
│  │  ✓ 重點五    ║  ✓ 重點五   ║  ✓ 重點五    │             │
│  └──────────────╚═════════════╝──────────────┘             │
│  ─────────────────────────────────────────────────────────  │
└─────────────────────────────────────────────────────────────┘
```

## 適用情境

- 三大核心優勢：並排展示品牌三個差異化競爭優勢
- 三個核心價值：呈現企業文化或服務理念的三大支柱
- 三種解決方案：對比三個方案的主要特性與適用情境

## Core Prompt

```
Generate a three-pillar columns slide (16:9, 13.33" × 7.50"):

=== TITLE AREA ===
Title text: "{slide_title}" — 28pt, Bold, {title_color}
  Position: x=0.50", y=0.30", width=12.30", height=0.60"
Title underline:
  Rectangle: x=0.50", y=1.00", width=12.30", height=0.04"
  Fill: {accent_color}

=== THREE COLUMN LAYOUT ===
Content area: x=0.50", y=1.15", width=12.30", height=5.90"
Column width: 4.10" each (three equal columns)
Column x positions: 0.50", 4.60", 8.70"

For each column {c} (c=1, 2, 3):
  Column background:
    If c == {emphasis_col} (emphasized center or other column):
      Rectangle: x=col_x, y=1.15", width=4.10", height=5.90"
      Fill: {emphasis_bg_color}
    Else:
      Rectangle: x=col_x, y=1.15", width=4.10", height=5.90"
      Fill: {col_bg_color}

  Icon placeholder (top center of column):
    Circle: x=col_x+1.67", y=1.35", width=0.76", height=0.76"
    Fill: {icon_color_c}
    (Use {icon_color_emphasis} for emphasized column)

  Column title:
    Text: "{col_title_c}" — 20pt, Bold, {col_title_color_c}
    Position: x=col_x+0.15", y=2.25", width=3.80", height=0.56"
    Align: center

  Title underline (optional, decorative):
    Rectangle: x=col_x+0.60", y=2.85", width=2.90", height=0.04"
    Fill: {col_underline_color_c}

  Checkmark items (3–5 items):
    For each item {k} (k=1 to item_count):
      Checkmark symbol "✓":
        Text: "✓" — 13pt, Bold, {check_color_c}
        Position: x=col_x+0.20", y=item_y, width=0.30", height=0.36"
      Item text: "{col_item_c_k}" — 12pt, normal, {item_text_color_c}
        Position: x=col_x+0.55", y=item_y, width=3.35", height=0.36"
      item_y starts at 3.00" and increments by 0.44" per item

=== COLUMN DIVIDERS ===
Vertical dividers between columns:
  Rectangle: x=4.58", y=1.15", width=0.03", height=5.90", Fill: {divider_color}
  Rectangle: x=8.68", y=1.15", width=0.03", height=5.90", Fill: {divider_color}

=== BOTTOM RULE ===
Thin rectangle: x=0.50", y=7.10", width=12.30", height=0.05"
Fill: {bottom_rule_color}

Bottom decoration:
Thin rectangle: x=0.50", y=7.18", width=12.30", height=0.05"
Fill: {bottom_line_color}

Content to fill in:
Emphasized column: {emphasis_col} (1, 2, or 3; set to 0 to disable)
{columns_content}
  Format:
  Column 1: title="{col_title_1}", items=["{item_1}", "{item_2}", ..., "{item_5}"]
  Column 2: title="{col_title_2}", items=["{item_1}", "{item_2}", ..., "{item_5}"]
  Column 3: title="{col_title_3}", items=["{item_1}", "{item_2}", ..., "{item_5}"]
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 投影片整體標題 | `三大核心競爭優勢` |
| `{title_color}` | 主標題文字色 | `#404040` |
| `{accent_color}` | 標題底線色 | `#0091D5` |
| `{col_bg_color}` | 一般欄位背景色 | `#F7FAFF`（極淺藍）或 `#FFFFFF` |
| `{emphasis_col}` | 強調欄位編號（1、2 或 3，0 代表不強調） | `2` |
| `{emphasis_bg_color}` | 強調欄位背景色 | `#E8F4FD` 或 `#1B4F9B`（深色） |
| `{icon_color_c}` | 第 c 欄圖示佔位符顏色 | `#0091D5` |
| `{icon_color_emphasis}` | 強調欄圖示顏色 | `#1B4F9B` |
| `{col_title_c}` | 第 c 欄標題 | `效率領先` |
| `{col_title_color_c}` | 第 c 欄標題文字色 | `#1B4F9B` |
| `{col_underline_color_c}` | 第 c 欄標題底線裝飾色 | `#0091D5` |
| `{check_color_c}` | 第 c 欄 checkmark 符號色 | `#0091D5` |
| `{col_item_c_k}` | 第 c 欄第 k 個重點 | `全球 180+ 航線覆蓋` |
| `{item_text_color_c}` | 第 c 欄重點文字色 | `#404040` |
| `{divider_color}` | 欄間分隔線色 | `#CCCCCC` |
| `{bottom_rule_color}` | 底部橫線色（欄底收尾） | `#0091D5` |
| `{bottom_line_color}` | 底部極淺裝飾線色 | `#E8F4FD` |
| `{brand_name}` | 品牌名稱 | `（替換為實際品牌名）` |

## python-pptx 程式碼骨架

```python
def build_three_columns(slide, s: dict):
    """
    建立三欄支柱 / 三大亮點版型

    Args:
        slide: 空白投影片物件
        s: dict，包含以下欄位：
            slide_title (str): 投影片標題
            columns (list): 三欄資料列表，每項為
                {"title": str, "items": [str, ...]}，最多 5 個 items
            emphasis_col (int): 強調欄編號（1–3），0 為不強調，預設 2
            emphasis_bg_color (tuple): 強調欄背景 RGB，預設 (232, 244, 253)
            accent_color (tuple): 主強調色 RGB，預設 (0, 145, 213)
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    accent = RGBColor(*s.get("accent_color", (0, 145, 213)))
    navy = RGBColor(27, 79, 155)
    dark = RGBColor(64, 64, 64)
    white = RGBColor(255, 255, 255)
    divider = RGBColor(0xCC, 0xCC, 0xCC)
    col_bg = RGBColor(0xF7, 0xFA, 0xFF)
    emphasis_bg = RGBColor(*s.get("emphasis_bg_color", (0xE8, 0xF4, 0xFD)))
    bottom_line = RGBColor(0xE8, 0xF4, 0xFD)

    # — 標題 —
    add_text(slide, s["slide_title"],
             Inches(0.50), Inches(0.30), Inches(12.30), Inches(0.60),
             font_size=28, bold=True, color=dark, align="left", font_name="Calibri")
    add_rect(slide, Inches(0.50), Inches(1.00), Inches(12.30), Inches(0.04),
             fill_color=accent)

    emphasis_col = s.get("emphasis_col", 2)
    columns = s.get("columns", [])[:3]
    col_xs = [0.50, 4.60, 8.70]
    col_w = 4.10

    for i, col in enumerate(columns):
        cx = col_xs[i]
        is_emphasis = (emphasis_col == i + 1)
        bg = emphasis_bg if is_emphasis else col_bg
        icon_color = navy if is_emphasis else accent
        title_color = navy
        check_color = navy if is_emphasis else accent

        # 欄位背景
        add_rect(slide, Inches(cx), Inches(1.15),
                 Inches(col_w), Inches(5.90), fill_color=bg)

        # 圖示佔位符
        add_rect(slide, Inches(cx + 1.67), Inches(1.35),
                 Inches(0.76), Inches(0.76), fill_color=icon_color)

        # 欄位標題
        add_text(slide, col.get("title", ""),
                 Inches(cx + 0.15), Inches(2.25),
                 Inches(col_w - 0.30), Inches(0.56),
                 font_size=20, bold=True, color=title_color,
                 align="center", font_name="Calibri")

        # 標題底線
        add_rect(slide, Inches(cx + 0.60), Inches(2.85),
                 Inches(2.90), Inches(0.04), fill_color=accent)

        # Checkmark 重點列表
        items = col.get("items", [])[:5]
        item_y = 3.00
        for item in items:
            add_text(slide, "✓",
                     Inches(cx + 0.20), Inches(item_y),
                     Inches(0.30), Inches(0.36),
                     font_size=13, bold=True, color=check_color,
                     align="left", font_name="Calibri")
            add_text(slide, item,
                     Inches(cx + 0.55), Inches(item_y),
                     Inches(col_w - 0.65), Inches(0.36),
                     font_size=12, bold=False, color=dark,
                     align="left", font_name="Calibri")
            item_y += 0.44

    # 欄間分隔線
    for vx in [4.58, 8.68]:
        add_rect(slide, Inches(vx), Inches(1.15), Inches(0.03), Inches(5.90),
                 fill_color=divider)

    # 底部橫線（欄底收尾）
    add_rect(slide, Inches(0.50), Inches(7.10), Inches(12.30), Inches(0.05),
             fill_color=accent)

    # — 底部裝飾線 —
    add_rect(slide, Inches(0.50), Inches(7.18), Inches(12.30), Inches(0.05),
             fill_color=bottom_line)
```

## 範例

### 輸入範例

```
標題：{brand_name} 三大核心競爭優勢

emphasis_col: 2

Column 1: title="效率領先"
  items:
    - "全球 180+ 條航線覆蓋"
    - "海運艙位優先保障"
    - "平均轉運時效縮短 30%"
    - "電子化即時追蹤系統"

Column 2: title="安全可靠"（強調欄）
  items:
    - "AEO 國際安全認證"
    - "CCTV 出貨全程錄影"
    - "ISO 9001 品質管理"
    - "貨損理賠率 < 0.01%"
    - "24 小時緊急應變團隊"

Column 3: title="彈性服務"
  items:
    - "客製化包裝與標籤"
    - "倉儲代管彈性方案"
    - "FCL / LCL 靈活選擇"
    - "電商逆物流整合"
```

### 輸出效果

白底，藍色粗體標題與底線，三欄等寬並排，淺灰細線分隔，
中間欄使用淺藍背景強調，每欄頂部有品牌藍色圓形圖示佔位符，
欄位大標題下方有藍色裝飾底線，
四到五個 checkmark 條列以清單形式呈現各欄重點，
底部藍色橫線與極淺裝飾線雙層收尾。
