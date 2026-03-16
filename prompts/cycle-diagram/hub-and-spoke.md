---
layout: cycle_diagram
name: 環狀循環圖 / 中心輻射
tags: [cycle, hub-and-spoke, radial, ecosystem, relationship]
---

# 環狀循環圖 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│  標題文字  28pt Bold                                         │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│      ╭───╮              ╭───╮              ╭───╮            │
│      │ A │              │ B │              │ C │            │
│      ╰─┬─╯              ╰─┬─╯              ╰─┬─╯            │
│        └──────────┐  ┌───┘                  │              │
│                   │  │                      │              │
│             ╭─────┴──┴─────╮                │              │
│      ╭──────┤  核心概念     ├──────────────── ╯             │
│      │      ╰─────┬──┬─────╯                               │
│      │            │  │                                     │
│    ╭─┴─╮        ╭─┴─╮╭─┴─╮                                │
│    │ D │        │ E ││ F │                                 │
│    ╰───╯        ╰───╯╰───╯                                 │
│                                                              │
│  ─────────────────────────────────────────────────────────  │
└─────────────────────────────────────────────────────────────┘
```

## 適用情境

- 生態系統展示：以核心平台為中心，呈現各合作夥伴或功能模組
- 核心能力輻射：一個核心競爭優勢帶動多個業務面向
- 循環業務關係：展示各部門或服務之間的相互依存關係

## Core Prompt

```
Generate a hub-and-spoke cycle diagram slide (16:9, 13.33" × 7.50"):

=== TITLE AREA ===
Title text: "{slide_title}" — 28pt, Bold, {title_color}
  Position: x=0.50", y=0.30", width=12.30", height=0.60"
Title underline:
  Rectangle: x=0.50", y=1.00", width=12.30", height=0.04"
  Fill: {accent_color}

=== HUB (CENTER CIRCLE) ===
Center of diagram: cx=6.67", cy=4.10"
Hub circle: cx-0.90" to cx+0.90", cy-0.90" to cy+0.90"
  Rectangle approximation: x=5.77", y=3.20", width=1.80", height=1.80"
  Fill: {hub_color}
  (Use oval/ellipse shape for best result)
Hub text: "{hub_text}" — 16pt, Bold, white
  Position: x=5.77", y=3.62", width=1.80", height=0.56"
  Align: center
Hub subtitle (optional): "{hub_subtitle}" — 11pt, normal, white
  Position: x=5.77", y=4.18", width=1.80", height=0.32"
  Align: center

=== SPOKE NODES ===
Total spoke nodes: {spoke_count} (4–6 recommended)
Node circle diameter: 1.10" (radius 0.55")
Node positions: evenly distributed on a circle of radius {spoke_radius} from center
  Suggested spoke_radius: 2.40" for 4 nodes, 2.50" for 5–6 nodes
  Angle offset: 0° at top, clockwise distribution

For each spoke node {k} (k=1 to spoke_count):
  angle_k = (k-1) * 360° / spoke_count  (0° = top)
  node_cx = hub_cx + spoke_radius * sin(angle_k)
  node_cy = hub_cy - spoke_radius * cos(angle_k)

  Connector line: from hub edge to node edge
    Line: x=hub_cx, y=hub_cy → x=node_cx, y=node_cy
    Width: 0.04", Fill: {connector_color}
    (Implemented as thin rectangle rotated to angle)

  Node circle:
    x=node_cx-0.55", y=node_cy-0.55", width=1.10", height=1.10"
    Fill: {spoke_color} (use alternating shades if desired)
    (Use oval/ellipse shape for best result)

  Node icon placeholder (optional):
    Rectangle: x=node_cx-0.22", y=node_cy-0.38", width=0.44", height=0.44"
    Fill: white with 40% opacity (for icon area)

  Node title (below or beside circle):
    Text: "{spoke_title_k}" — 13pt, Bold, {spoke_title_color}
      If node is in top half: place below circle
        Position: x=node_cx-0.70", y=node_cy+0.58", width=1.40", height=0.36"
      If node is in bottom half: place above circle
        Position: x=node_cx-0.70", y=node_cy-0.94", width=1.40", height=0.36"
      Align: center

  Node description (optional, 1 line):
    Text: "{spoke_desc_k}" — 10pt, normal, {spoke_desc_color}
      Position: adjacent to title, same side as title
      width=1.60", height=0.28"
      Align: center

=== BOTTOM DECORATION ===
Thin rectangle: x=0.50", y=7.18", width=12.30", height=0.05"
Fill: {bottom_line_color}

Content to fill in:
Hub: text="{hub_text}", subtitle="{hub_subtitle}"
{spokes_content}
  Format:
  Spoke 1: title="{spoke_title_1}", desc="{spoke_desc_1}"
  Spoke 2: title="{spoke_title_2}", desc="{spoke_desc_2}"
  ... (4–6 spokes)
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 投影片主標題 | `{brand_name} 服務生態系統` |
| `{title_color}` | 主標題文字色 | `#404040` |
| `{accent_color}` | 標題底線色 | `#0091D5` |
| `{hub_text}` | 中央圓形主文字 | `核心平台` |
| `{hub_subtitle}` | 中央圓形副文字（可省略） | `{brand_name}` |
| `{hub_color}` | 中央圓形填色（品牌主色） | `#1B4F9B` |
| `{spoke_count}` | 外圍節點數（4–6） | `5` |
| `{spoke_radius}` | 輻射半徑（英吋） | `2.50` |
| `{spoke_color}` | 外圍節點圓形填色（強調色） | `#0091D5` |
| `{connector_color}` | 連接線顏色 | `#AACCE8` |
| `{spoke_title_k}` | 第 k 個外圍節點標題 | `物流管理` |
| `{spoke_title_color}` | 外圍節點標題文字色 | `#1B4F9B` |
| `{spoke_desc_k}` | 第 k 個外圍節點說明（1 行） | `全自動倉儲與配送追蹤` |
| `{spoke_desc_color}` | 外圍節點說明文字色 | `#666666` |
| `{bottom_line_color}` | 底部裝飾線色（極淺） | `#E8F4FD` |
| `{brand_name}` | 品牌名稱 | `（替換為實際品牌名）` |

## python-pptx 程式碼骨架

```python
def build_cycle_diagram(slide, s: dict):
    """
    建立環狀循環圖 / 中心輻射版型

    Args:
        slide: 空白投影片物件
        s: dict，包含以下欄位：
            slide_title (str): 投影片標題
            hub_text (str): 中央圓形主文字
            hub_subtitle (str): 中央圓形副文字（可省略）
            spokes (list): 外圍節點列表，每項為 {"title": str, "desc": str}
            hub_color (tuple): 中央圓形 RGB，預設 (27, 79, 155)
            spoke_color (tuple): 外圍節點 RGB，預設 (0, 145, 213)
    """
    import math
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    hub_color = RGBColor(*s.get("hub_color", (27, 79, 155)))
    spoke_color = RGBColor(*s.get("spoke_color", (0, 145, 213)))
    connector_color = RGBColor(0xAA, 0xCC, 0xE8)
    dark = RGBColor(64, 64, 64)
    navy = RGBColor(27, 79, 155)
    mid = RGBColor(102, 102, 102)
    white = RGBColor(255, 255, 255)
    accent = RGBColor(0, 145, 213)
    bottom_line = RGBColor(0xE8, 0xF4, 0xFD)

    # — 標題 —
    add_text(slide, s["slide_title"],
             Inches(0.50), Inches(0.30), Inches(12.30), Inches(0.60),
             font_size=28, bold=True, color=dark, align="left", font_name="Calibri")
    add_rect(slide, Inches(0.50), Inches(1.00), Inches(12.30), Inches(0.04),
             fill_color=accent)

    hub_cx = 6.67
    hub_cy = 4.10
    hub_r = 0.90

    spokes = s.get("spokes", [])[:6]
    n = len(spokes)
    spoke_radius = 2.50 if n >= 5 else 2.40

    # — 連接線（先畫，讓圓形蓋在上方）—
    for i in range(n):
        angle = math.radians(i * 360 / n)
        nx = hub_cx + spoke_radius * math.sin(angle)
        ny = hub_cy - spoke_radius * math.cos(angle)

        # 計算連接線端點（從 hub 邊緣到 spoke 邊緣）
        dx = nx - hub_cx
        dy = ny - hub_cy
        dist = math.sqrt(dx * dx + dy * dy)
        start_x = hub_cx + dx * hub_r / dist
        start_y = hub_cy + dy * hub_r / dist
        end_x = nx - dx * 0.55 / dist
        end_y = ny - dy * 0.55 / dist

        # 用極細矩形近似連接線
        line_len = math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)
        mid_x = (start_x + end_x) / 2
        mid_y = (start_y + end_y) / 2
        add_rect(slide, Inches(mid_x - line_len / 2), Inches(mid_y - 0.02),
                 Inches(line_len), Inches(0.04),
                 fill_color=connector_color)

    # — 外圍節點 —
    for i, spoke in enumerate(spokes):
        angle = math.radians(i * 360 / n)
        nx = hub_cx + spoke_radius * math.sin(angle)
        ny = hub_cy - spoke_radius * math.cos(angle)

        add_rect(slide, Inches(nx - 0.55), Inches(ny - 0.55),
                 Inches(1.10), Inches(1.10), fill_color=spoke_color)
        add_text(slide, spoke.get("title", ""),
                 Inches(nx - 0.55), Inches(ny - 0.22),
                 Inches(1.10), Inches(0.44),
                 font_size=12, bold=True, color=white, align="center", font_name="Calibri")

        # 說明文字（依位置決定上方或下方）
        if ny <= hub_cy:
            desc_y = ny + 0.58
        else:
            desc_y = ny - 0.94

        add_text(slide, spoke.get("desc", ""),
                 Inches(nx - 0.80), Inches(desc_y),
                 Inches(1.60), Inches(0.28),
                 font_size=10, bold=False, color=mid, align="center", font_name="Calibri")

    # — 中央 Hub 圓形 —
    add_rect(slide, Inches(hub_cx - hub_r), Inches(hub_cy - hub_r),
             Inches(hub_r * 2), Inches(hub_r * 2), fill_color=hub_color)
    add_text(slide, s.get("hub_text", ""),
             Inches(hub_cx - hub_r), Inches(hub_cy - 0.28),
             Inches(hub_r * 2), Inches(0.56),
             font_size=16, bold=True, color=white, align="center", font_name="Calibri")
    if s.get("hub_subtitle"):
        add_text(slide, s["hub_subtitle"],
                 Inches(hub_cx - hub_r), Inches(hub_cy + 0.28),
                 Inches(hub_r * 2), Inches(0.32),
                 font_size=11, bold=False, color=white, align="center", font_name="Calibri")

    # — 底部裝飾線 —
    add_rect(slide, Inches(0.50), Inches(7.18), Inches(12.30), Inches(0.05),
             fill_color=bottom_line)
```

## 範例

### 輸入範例

```
標題：{brand_name} 一站式物流服務生態系統

Hub：text="核心平台", subtitle="{brand_name}"

外圍節點（5 個）：
  Spoke 1: title="海運進出口", desc="FCL／LCL 全球運籌"
  Spoke 2: title="空運快遞", desc="時效性高價值貨物"
  Spoke 3: title="倉儲管理", desc="智慧倉庫即時庫存"
  Spoke 4: title="報關服務", desc="AEO 認證快速通關"
  Spoke 5: title="電商代運", desc="跨境電商全流程支援"
```

### 輸出效果

白底，藍色粗體標題與底線，版面中央一個深藍色大圓形顯示「核心平台」，
五個品牌藍色外圍圓形以輻射狀等距分布，淺藍連線連結中心與各節點，
每個外圍節點內有白色粗體標題，節點旁有小字說明，
底部淺藍極細裝飾線收尾。
