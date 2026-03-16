---
layout: two_columns
tags: [two-columns, before-after, comparison, contrast, proposal]
updated: 2026-03-16
---

# Two Columns — 雙欄對比頁 (Before / After Contrast)

## 版面規格

```
┌─────────────────────────────────────────────────┐
│ [brand_name]    {slide_title}                   │ ← 頂部細色條 + 標題
│                                                 │
│ ┌──────────────────┐ ┌──────────────────────┐   │
│ │ {left_title}     │ │ {right_title}        │   │ ← 欄標題（各自色塊）
│ │──────────────────│ │──────────────────────│   │
│ │ • {left_bullet1} │ │ • {right_bullet1}    │   │
│ │ • {left_bullet2} │ │ • {right_bullet2}    │   │
│ │ • {left_bullet3} │ │ • {right_bullet3}    │   │
│ │ • {left_bullet4} │ │ • {right_bullet4}    │   │
│ └──────────────────┘ └──────────────────────┘   │
└─────────────────────────────────────────────────┘
```

**畫布尺寸：** 33.87 × 19.05 cm（16:9 寬螢幕）
**設計原則：** 左右等寬，強烈視覺對比，每欄最多 6 條

---

## Core Prompt

Create a **two-column contrast slide** that places two opposing concepts side-by-side with clear visual differentiation. Ideal for Before/After comparisons, Problem/Solution framing, or Option A/B decisions.

**Visual Structure:**
- Background: white
- Top edge: thin `{accent_color}` bar
- Slide title: `{slide_title}` at 24pt, bold
- Left column: `{left_color}` header block, `{left_title}` in white
- Right column: `{right_color}` header block, `{right_title}` in white
- Column body: light grey background with bullet items, 14pt
- Each column: max 6 bullet items

**Design Guidance:**
- Left = negative/problem/before → use dark navy or muted color
- Right = positive/solution/after → use brand accent or green
- Keep bullets parallel in structure for clean comparison
- Avoid more than 6 items per column to prevent clutter

---

## 變數說明

| 變數 | 說明 | 範例 |
|------|------|------|
| `{logo_text}` | 左上角品牌標識 | `MY BRAND` |
| `{slide_title}` | 頁面標題 | `導入前 vs. 導入後` |
| `{accent_color}` | 頂部色條色 | `#1B4F9B` |
| `{left_title}` | 左欄標題 | `導入前痛點` |
| `{left_color}` | 左欄標題色塊 | `#2D415F` |
| `{right_title}` | 右欄標題 | `導入後效益` |
| `{right_color}` | 右欄標題色塊 | `#1E6B3C` |
| `{left_column.bullets}` | 左欄條列（最多 6 條） | `["人工追蹤耗時", "資訊不透明"]` |
| `{right_column.bullets}` | 右欄條列（最多 6 條） | `["即時追蹤", "自動報表"]` |
| `{col_bg}` | 欄內容背景色 | `#F7F9FC` |

---

## python-pptx 骨架

```python
{
  "layout": "two_columns",
  "logo_text": "{logo_text}",
  "slide_title": "{slide_title}",
  "accent_color": "{accent_color}",
  "left_color": "{left_color}",
  "right_color": "{right_color}",
  "left_column": {
    "title": "{left_title}",
    "bullets": ["{left_bullet1}", "{left_bullet2}", "{left_bullet3}"]
  },
  "right_column": {
    "title": "{right_title}",
    "bullets": ["{right_bullet1}", "{right_bullet2}", "{right_bullet3}"]
  }
}
```

---

## 適用情境

- **對外商業提案**：痛點 vs. 解方對比，建立問題意識
- **內部策略會議**：競品比較、方案 A/B 決策
- **專業授課**：概念對比，降低認知負荷
