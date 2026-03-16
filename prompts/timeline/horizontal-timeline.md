---
layout: timeline
name: 橫向時間軸 / 里程碑
tags: [timeline, horizontal, milestone, history]
---

# 橫向時間軸 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│  標題文字  28pt Bold                                         │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│  ┌ 2019 ─────┐         ┌ 2021 ─────┐         ┌ 2023 ─────┐ │
│  │ 短標題一  │         │ 短標題三  │         │ 短標題五  │ │
│  │ 一行說明  │         │ 一行說明  │         │ 一行說明  │ │
│  └───────────┘         └───────────┘         └───────────┘ │
│          ●─────────────────●─────────────────●             │
│   ════════════════════════════════════════════════          │
│          ●─────────────────●                               │
│  ┌ 2020 ─────┐         ┌ 2022 ─────┐                       │
│  │ 短標題二  │         │ 短標題四  │                       │
│  │ 一行說明  │         │ 一行說明  │                       │
│  └───────────┘         └───────────┘                       │
│                                                              │
│  ───┬───────────┬───────────┬───────────┬───────────┬───   │
│   2019        2020        2021        2022        2023      │
└─────────────────────────────────────────────────────────────┘
```

## 適用情境

- 公司發展歷程：展示從創立至今的重要里程碑
- 產品迭代記錄：各版本發布時間與功能亮點
- 專案時程回顧：關鍵節點的達成狀況

## Core Prompt

```
Generate a horizontal timeline milestone slide (16:9, 13.33" × 7.50"):

=== TITLE AREA ===
Title text: "{slide_title}" — 28pt, Bold, {title_color}
  Position: x=0.50", y=0.30", width=12.30", height=0.60"
Title underline:
  Rectangle: x=0.50", y=1.00", width=12.30", height=0.04"
  Fill: {accent_color}

=== CENTRAL TIMELINE BAR ===
Horizontal bar: x=0.80", y=3.60", width=11.70", height=0.06"
Fill: {timeline_color}

=== TIME SCALE TICKS (bottom) ===
Tick line: x=0.80", y=6.20", width=11.70", height=0.04"
Fill: {tick_color}
For each node {n}, place a vertical tick mark at x=node_x, y=6.20", width=0.04", height=0.16"
Place year label "{year_n}" at x=node_x-0.20", y=6.40", width=0.50", height=0.24"
  Font: 11pt, {label_color}

=== TIMELINE NODES (alternating above/below) ===
Total nodes: {node_count} (4–6 recommended)
Node x positions: evenly distributed between x=1.00" and x=12.50"

For each ODD node {n} (1, 3, 5 — above the line):
  Circle marker: center at (node_x, 3.60"), diameter=0.26"
    Fill: {marker_color}, no border
  Connector line: x=node_x-0.02", y=2.10", width=0.04", height=1.50"
    Fill: {connector_color}
  Label box (above):
    Year/date: "{date_n}" — 12pt, Bold, {date_color}
      Position: x=node_x-0.60", y=1.45", width=1.20", height=0.30"
    Title: "{node_title_n}" — 13pt, Bold, {node_title_color}
      Position: x=node_x-0.80", y=1.75", width=1.60", height=0.32"
    Description: "{node_desc_n}" — 11pt, normal, {node_desc_color}
      Position: x=node_x-0.80", y=2.07", width=1.60", height=0.28"

For each EVEN node {n} (2, 4, 6 — below the line):
  Circle marker: center at (node_x, 3.60"), diameter=0.26"
    Fill: {marker_color_alt}, no border
  Connector line: x=node_x-0.02", y=3.66", width=0.04", height=1.50"
    Fill: {connector_color}
  Label box (below):
    Year/date: "{date_n}" — 12pt, Bold, {date_color}
      Position: x=node_x-0.60", y=5.16", width=1.20", height=0.30"
    Title: "{node_title_n}" — 13pt, Bold, {node_title_color}
      Position: x=node_x-0.80", y=5.46", width=1.60", height=0.32"
    Description: "{node_desc_n}" — 11pt, normal, {node_desc_color}
      Position: x=node_x-0.80", y=5.78", width=1.60", height=0.28"

=== BOTTOM DECORATION ===
Thin rectangle: x=0.50", y=7.18", width=12.30", height=0.05"
Fill: {bottom_line_color}

Content to fill in:
{timeline_nodes}
  Format per node:
  Node 1: date="{date_1}", title="{title_1}", desc="{desc_1}"
  Node 2: date="{date_2}", title="{title_2}", desc="{desc_2}"
  ... (up to 6 nodes)
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 投影片主標題 | `{brand_name} 發展里程碑` |
| `{title_color}` | 主標題文字色 | `#404040` |
| `{accent_color}` | 標題底線色 | `#0091D5` |
| `{timeline_color}` | 中央時間線色 | `#0091D5` |
| `{tick_color}` | 底部刻度線色 | `#CCCCCC` |
| `{label_color}` | 底部年份標籤色 | `#888888` |
| `{marker_color}` | 奇數節點圓形標記色（品牌主色） | `#0091D5` |
| `{marker_color_alt}` | 偶數節點圓形標記色（品牌強調色） | `#1B4F9B` |
| `{connector_color}` | 節點連接線色 | `#CCCCCC` |
| `{date_color}` | 年份 / 日期文字色 | `#0091D5` |
| `{node_title_color}` | 節點標題文字色 | `#404040` |
| `{node_desc_color}` | 節點說明文字色 | `#666666` |
| `{bottom_line_color}` | 底部裝飾線色（極淺） | `#E8F4FD` |
| `{node_count}` | 節點總數（4–6） | `5` |
| `{date_n}` | 第 n 個節點的年份或日期 | `2021` |
| `{node_title_n}` | 第 n 個節點標題（10 字以內） | `正式上市` |
| `{node_desc_n}` | 第 n 個節點說明（一行） | `推出旗艦產品，首月出貨破萬` |
| `{brand_name}` | 品牌名稱 | `（替換為實際品牌名）` |

## python-pptx 程式碼骨架

```python
def build_timeline(slide, s: dict):
    """
    建立橫向時間軸 / 里程碑版型

    Args:
        slide: 空白投影片物件
        s: dict，包含以下欄位：
            slide_title (str): 投影片標題
            nodes (list): 節點列表，每項為 {"date": str, "title": str, "desc": str}
            accent_color (tuple): 主強調色 RGB，預設 (0, 145, 213)
            marker_color_alt (tuple): 偶數節點色 RGB，預設 (27, 79, 155)
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    accent = RGBColor(*s.get("accent_color", (0, 145, 213)))
    alt = RGBColor(*s.get("marker_color_alt", (27, 79, 155)))
    dark = RGBColor(64, 64, 64)
    mid = RGBColor(102, 102, 102)
    light = RGBColor(204, 204, 204)

    # — 標題 —
    add_text(slide, s["slide_title"],
             Inches(0.50), Inches(0.30), Inches(12.30), Inches(0.60),
             font_size=28, bold=True, color=dark, align="left", font_name="Calibri")
    add_rect(slide, Inches(0.50), Inches(1.00), Inches(12.30), Inches(0.04),
             fill_color=accent)

    # — 中央時間線 —
    add_rect(slide, Inches(0.80), Inches(3.57), Inches(11.70), Inches(0.06),
             fill_color=accent)

    # — 底部刻度線 —
    add_rect(slide, Inches(0.80), Inches(6.20), Inches(11.70), Inches(0.03),
             fill_color=light)

    nodes = s.get("nodes", [])[:6]
    n_count = len(nodes)
    if n_count == 0:
        return

    x_start = 1.00
    x_end = 12.50
    step = (x_end - x_start) / max(n_count - 1, 1)

    for i, node in enumerate(nodes):
        nx = x_start + i * step
        is_above = (i % 2 == 0)
        marker_color = accent if is_above else alt

        # 圓形標記（用正方形近似，實際可改橢圓）
        add_rect(slide, Inches(nx - 0.13), Inches(3.47), Inches(0.26), Inches(0.26),
                 fill_color=marker_color)

        # 底部刻度
        add_rect(slide, Inches(nx - 0.02), Inches(6.20), Inches(0.04), Inches(0.16),
                 fill_color=light)
        add_text(slide, node.get("date", ""),
                 Inches(nx - 0.25), Inches(6.38), Inches(0.50), Inches(0.24),
                 font_size=10, bold=False, color=mid, align="center", font_name="Calibri")

        if is_above:
            # 連接線
            add_rect(slide, Inches(nx - 0.02), Inches(2.10), Inches(0.04), Inches(1.47),
                     fill_color=light)
            # 文字標籤（上方）
            add_text(slide, node.get("date", ""),
                     Inches(nx - 0.60), Inches(1.45), Inches(1.20), Inches(0.30),
                     font_size=12, bold=True, color=accent, align="center", font_name="Calibri")
            add_text(slide, node.get("title", ""),
                     Inches(nx - 0.80), Inches(1.75), Inches(1.60), Inches(0.32),
                     font_size=13, bold=True, color=dark, align="center", font_name="Calibri")
            add_text(slide, node.get("desc", ""),
                     Inches(nx - 0.80), Inches(2.07), Inches(1.60), Inches(0.28),
                     font_size=11, bold=False, color=mid, align="center", font_name="Calibri")
        else:
            # 連接線
            add_rect(slide, Inches(nx - 0.02), Inches(3.63), Inches(0.04), Inches(1.57),
                     fill_color=light)
            # 文字標籤（下方）
            add_text(slide, node.get("date", ""),
                     Inches(nx - 0.60), Inches(5.20), Inches(1.20), Inches(0.30),
                     font_size=12, bold=True, color=alt, align="center", font_name="Calibri")
            add_text(slide, node.get("title", ""),
                     Inches(nx - 0.80), Inches(5.50), Inches(1.60), Inches(0.32),
                     font_size=13, bold=True, color=dark, align="center", font_name="Calibri")
            add_text(slide, node.get("desc", ""),
                     Inches(nx - 0.80), Inches(5.82), Inches(1.60), Inches(0.28),
                     font_size=11, bold=False, color=mid, align="center", font_name="Calibri")

    # — 底部裝飾線 —
    add_rect(slide, Inches(0.50), Inches(7.18), Inches(12.30), Inches(0.05),
             fill_color=RGBColor(0xE8, 0xF4, 0xFD))
```

## 範例

### 輸入範例

```
標題：{brand_name} 十年發展里程碑

節點1：date="2015", title="公司成立", desc="於台北市正式登記設立"
節點2：date="2017", title="首個產品上市", desc="推出旗艦產品，首月出貨破萬"
節點3：date="2019", title="海外展點", desc="進駐東南亞三大市場"
節點4：date="2021", title="Series B 募資", desc="完成 5,000 萬美元融資"
節點5：date="2023", title="上市掛牌", desc="於台灣證券交易所正式掛牌"
```

### 輸出效果

白底，藍色粗體標題與底線，中央細長藍色橫線貫穿版面，
五個節點以奇上偶下交替排列，奇數節點藍色圓標記附上方年份與說明，
偶數節點深藍圓標記附下方說明，底部灰色刻度線標示各年份，
最底部淺藍極細裝飾線收尾。
