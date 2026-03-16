---
layout: process_steps
name: 步驟流程圖
tags: [process, steps, numbered, workflow, arrow]
---

# 步驟流程圖 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│  標題文字  28pt Bold                                         │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│   ╔═══════╗    ▶    ╔═══════╗    ▶    ╔═══════╗    ▶   ╔══╗ │
│   ║  ①   ║         ║  ②   ║         ║  ③   ║         ║④║ │
│   ╠═══════╣         ╠═══════╣         ╠═══════╣         ╚══╝ │
│   ║ 步驟  ║         ║ 步驟  ║         ║ 步驟  ║  ◀完成▶     │
│   ║ 標題  ║         ║ 標題  ║         ║ 標題  ║             │
│   ║ 說明  ║         ║ 說明  ║         ║ 說明  ║             │
│   ║ 文字  ║         ║ 文字  ║         ║ 文字  ║             │
│   ╚═══════╝         ╚═══════╝         ╚═══════╝             │
│                                                              │
│  ─────────────────────────────────────────────────────────  │
└─────────────────────────────────────────────────────────────┘
```

## 適用情境

- 服務流程說明：從諮詢、報價到交付的完整步驟
- 操作指南：引導使用者完成多步驟設定流程
- 工作流程介紹：展示跨部門協作的標準化程序

## Core Prompt

```
Generate a numbered process steps slide (16:9, 13.33" × 7.50"):

=== TITLE AREA ===
Title text: "{slide_title}" — 28pt, Bold, {title_color}
  Position: x=0.50", y=0.30", width=12.30", height=0.60"
Title underline:
  Rectangle: x=0.50", y=1.00", width=12.30", height=0.04"
  Fill: {accent_color}

=== STEP BLOCKS ===
Total steps: {step_count} (3–5 recommended)
Content area: x=0.50" to x=12.80", y=1.20" to y=6.80"

Step block width = (12.30" - arrow_gaps) / step_count
Arrow width = 0.40", placed between each pair of steps

For each step {n}:
  Step block background:
    Rectangle: x=step_x, y=1.35", width=step_w, height=5.00"
    Fill: {step_bg_color}, border: {step_border_color} (0.5pt)

  Number badge (top center of block):
    Circle background: x=badge_cx-0.28", y=1.45", width=0.56", height=0.56"
      Fill: {badge_color}
    Badge text: "{n}" — 20pt, Bold, white
      Position: centered on badge

  Step title (below badge):
    Text: "{step_title_n}" — 15pt, Bold, {step_title_color}
      Position: x=step_x+0.10", y=2.15", width=step_w-0.20", height=0.44"
      Align: center

  Step description (below title):
    Text: "{step_desc_n}" — 12pt, normal, {step_desc_color}
      Position: x=step_x+0.12", y=2.65", width=step_w-0.24", height=2.50"
      Align: center, word wrap enabled

  If n == step_count (last step) and {show_result_badge} == true:
    Result highlight box:
      Rectangle: x=step_x-0.06", y=1.28", width=step_w+0.12", height=5.20"
      Fill: {result_bg_color}, border: {result_border_color} (2pt)
    Result label text: "{result_label}" — 11pt, Bold, {result_label_color}
      Position: x=step_x, y=6.52", width=step_w, height=0.28"
      Align: center

=== ARROWS BETWEEN STEPS ===
For each gap between steps (n=1 to step_count-1):
  Arrow triangle: x=arrow_x, y=3.60", width=0.38", height=0.38"
    Fill: {arrow_color}
    Shape: right-pointing triangle (▶)
    (Implemented as a narrow rectangle + triangle approximation)

=== BOTTOM DECORATION ===
Thin rectangle: x=0.50", y=7.18", width=12.30", height=0.05"
Fill: {bottom_line_color}

Content to fill in:
{steps_content}
  Format:
  Step 1: title="{step_title_1}", desc="{step_desc_1}"
  Step 2: title="{step_title_2}", desc="{step_desc_2}"
  Step 3: title="{step_title_3}", desc="{step_desc_3}"
  ... (up to 5 steps)
  Result label: "{result_label}" (optional, shown on last step)
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 投影片主標題 | `服務交付流程` |
| `{title_color}` | 主標題文字色 | `#404040` |
| `{accent_color}` | 標題底線與強調色 | `#0091D5` |
| `{step_count}` | 步驟總數（3–5） | `4` |
| `{step_bg_color}` | 步驟方塊背景色 | `#F0F7FF` |
| `{step_border_color}` | 步驟方塊邊框色 | `#CCE4F7` |
| `{badge_color}` | 數字徽章背景色（品牌色） | `#0091D5` |
| `{step_title_n}` | 第 n 步標題（行動動詞開頭） | `提交需求單` |
| `{step_title_color}` | 步驟標題文字色 | `#1B4F9B` |
| `{step_desc_n}` | 第 n 步說明（2–3 行） | `填寫線上表單，說明需求與預算` |
| `{step_desc_color}` | 步驟說明文字色 | `#555555` |
| `{arrow_color}` | 步驟間箭頭色 | `#0091D5` |
| `{show_result_badge}` | 是否在最後一步加強調框 | `true` |
| `{result_bg_color}` | 最後步驟強調框背景色 | `#E8F4FD` |
| `{result_border_color}` | 最後步驟強調框邊框色 | `#0091D5` |
| `{result_label}` | 最後步驟底部標籤 | `✓ 交付完成` |
| `{result_label_color}` | 最後步驟標籤文字色 | `#0091D5` |
| `{bottom_line_color}` | 底部裝飾線色（極淺） | `#E8F4FD` |
| `{brand_name}` | 品牌名稱（用於標題） | `（替換為實際品牌名）` |

## python-pptx 程式碼骨架

```python
def build_process_steps(slide, s: dict):
    """
    建立步驟流程圖版型

    Args:
        slide: 空白投影片物件
        s: dict，包含以下欄位：
            slide_title (str): 投影片標題
            steps (list): 步驟列表，每項為 {"title": str, "desc": str}
            show_result_badge (bool): 是否在最後一步加強調框，預設 True
            result_label (str): 最後步驟標籤文字，預設 "✓ 完成"
            accent_color (tuple): 主強調色 RGB，預設 (0, 145, 213)
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    accent = RGBColor(*s.get("accent_color", (0, 145, 213)))
    navy = RGBColor(27, 79, 155)
    dark = RGBColor(64, 64, 64)
    mid = RGBColor(85, 85, 85)
    white = RGBColor(255, 255, 255)
    bg_blue = RGBColor(0xF0, 0xF7, 0xFF)
    border_blue = RGBColor(0xCC, 0xE4, 0xF7)
    bottom_line = RGBColor(0xE8, 0xF4, 0xFD)

    # — 標題 —
    add_text(slide, s["slide_title"],
             Inches(0.50), Inches(0.30), Inches(12.30), Inches(0.60),
             font_size=28, bold=True, color=dark, align="left", font_name="Calibri")
    add_rect(slide, Inches(0.50), Inches(1.00), Inches(12.30), Inches(0.04),
             fill_color=accent)

    steps = s.get("steps", [])[:5]
    n = len(steps)
    if n == 0:
        return

    arrow_w = 0.40
    total_arrow_w = arrow_w * (n - 1)
    content_w = 12.30
    step_w = (content_w - total_arrow_w) / n

    x_start = 0.50
    show_result = s.get("show_result_badge", True)
    result_label = s.get("result_label", "✓ 完成")

    for i, step in enumerate(steps):
        sx = x_start + i * (step_w + arrow_w)
        is_last = (i == n - 1)

        # 強調框（最後步驟）
        if is_last and show_result:
            add_rect(slide, Inches(sx - 0.06), Inches(1.28),
                     Inches(step_w + 0.12), Inches(5.20),
                     fill_color=bg_blue, border_color=accent)
        else:
            add_rect(slide, Inches(sx), Inches(1.35),
                     Inches(step_w), Inches(5.00),
                     fill_color=bg_blue, border_color=border_blue)

        # 數字徽章
        badge_cx = sx + step_w / 2
        add_rect(slide, Inches(badge_cx - 0.28), Inches(1.45),
                 Inches(0.56), Inches(0.56), fill_color=accent)
        add_text(slide, str(i + 1),
                 Inches(badge_cx - 0.28), Inches(1.45), Inches(0.56), Inches(0.56),
                 font_size=20, bold=True, color=white, align="center", font_name="Calibri")

        # 步驟標題
        add_text(slide, step.get("title", ""),
                 Inches(sx + 0.10), Inches(2.15), Inches(step_w - 0.20), Inches(0.44),
                 font_size=15, bold=True, color=navy, align="center", font_name="Calibri")

        # 步驟說明
        add_text(slide, step.get("desc", ""),
                 Inches(sx + 0.12), Inches(2.65), Inches(step_w - 0.24), Inches(2.50),
                 font_size=12, bold=False, color=mid, align="center", font_name="Calibri")

        # 最後步驟底部標籤
        if is_last and show_result:
            add_text(slide, result_label,
                     Inches(sx), Inches(6.52), Inches(step_w), Inches(0.28),
                     font_size=11, bold=True, color=accent, align="center", font_name="Calibri")

        # 箭頭（不在最後一步後面）
        if not is_last:
            arrow_x = sx + step_w + 0.01
            add_rect(slide, Inches(arrow_x), Inches(3.72),
                     Inches(arrow_w - 0.02), Inches(0.24),
                     fill_color=accent)

    # — 底部裝飾線 —
    add_rect(slide, Inches(0.50), Inches(7.18), Inches(12.30), Inches(0.05),
             fill_color=bottom_line)
```

## 範例

### 輸入範例

```
標題：客戶服務交付流程

步驟1：title="提交需求", desc="填寫線上需求表單，說明目標與預算範圍"
步驟2：title="評估報價", desc="業務團隊於 2 個工作日內回覆專屬報價方案"
步驟3：title="簽約啟動", desc="確認合約條款，雙方簽署後立即排入執行時程"
步驟4：title="交付驗收", desc="依約完成交付，客戶確認後開立發票"

show_result_badge: true
result_label: "✓ 完成交付"
```

### 輸出效果

白底，藍色粗體標題與底線，四個等寬淡藍色步驟方塊橫向排列，
每個方塊頂部有品牌藍色數字圓形徽章，方塊內含粗體步驟標題與說明文字，
步驟間有藍色實心三角箭頭連線，最後一個步驟外框加粗強調並顯示「✓ 完成交付」標籤，
底部淺藍極細裝飾線收尾。
