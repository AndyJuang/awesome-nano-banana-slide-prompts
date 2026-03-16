---
layout: data_chart
tags: [data-chart, kpi, chart, data-visualization, internal]
updated: 2026-03-16
---

# Data Chart — 數據圖表佔位頁 (KPI + Chart Placeholder)

## 版面規格

```
┌─────────────────────────────────────────────────┐
│ [brand_name]    {slide_title}                   │ ← 頂部細色條 + 標題
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │ {kpi[0]} │ │ {kpi[1]} │ │ {kpi[2]} │         │ ← KPI 數字區塊（最多 3）
│ │  value   │ │  value   │ │  value   │         │
│ │  label   │ │  label   │ │  label   │         │
│ └──────────┘ └──────────┘ └──────────┘         │
│ ┌─────────────────────────────────────────────┐ │
│ │                                             │ │ ← 圖表佔位框
│ │   [ 圖表佔位：請在編輯器中插入實際圖表 ]     │ │
│ │                                             │ │
│ └─────────────────────────────────────────────┘ │
│ 資料來源：{source}                              │ ← 底部來源標注
└─────────────────────────────────────────────────┘
```

**畫布尺寸：** 33.87 × 19.05 cm（16:9 寬螢幕）
**設計原則：** KPI 數字視覺化，圖表以佔位框呈現，需在 Google Slides / PowerPoint 中插入實際圖表

---

## Core Prompt

Create a **data and chart slide** that showcases key performance indicators and provides a clearly labeled placeholder for chart insertion.

**Visual Structure:**
- Background: white
- Top edge: thin `{accent_color}` bar
- Top-left: `{logo_text}` in 9pt brand color
- Slide title: `{slide_title}` at 24pt, bold, near-top
- KPI blocks (up to 3): light-blue background cards, large value in `{accent_color}`, smaller label below
- Chart placeholder: light grey bordered box, centered instructional text
- Bottom: data source attribution in 10pt muted text

**Data Guidelines:**
- KPI values: emphasize with large font (42pt), avoid excessive decimal places
- Chart area: annotate chart type in the prompt (e.g., "line chart: revenue trend 2022-2026")
- Source: always cite data origin for credibility

---

## 變數說明

| 變數 | 說明 | 範例 |
|------|------|------|
| `{logo_text}` | 左上角品牌標識 | `MY BRAND` |
| `{slide_title}` | 頁面標題 | `2026 年業績成長概況` |
| `{accent_color}` | 強調色（KPI、色條） | `#1B4F9B` |
| `{kpis}` | KPI 陣列，每項含 value + label | `[{"value":"85%","label":"準時交付率"}]` |
| `{kpi_bg}` | KPI 卡片背景色 | `#EEF3FA` |
| `{chart_note}` | 圖表佔位說明文字 | `[ 折線圖：2022-2026 年營收趨勢 ]` |
| `{source}` | 資料來源（可省略） | `資料來源：內部財報 Q4 2025` |

---

## python-pptx 骨架

```python
{
  "layout": "data_chart",
  "logo_text": "{logo_text}",
  "slide_title": "{slide_title}",
  "accent_color": "{accent_color}",
  "kpis": [
    {"value": "{value_1}", "label": "{label_1}"},
    {"value": "{value_2}", "label": "{label_2}"},
    {"value": "{value_3}", "label": "{label_3}"}
  ],
  "chart_note": "[ {chart_type}：{chart_description} ]",
  "source": "{source}"
}
```

---

## 適用情境

- **內部策略與進度會議**：核心 KPI 與趨勢匯報
- **對外商業提案**：用數據建立信任感
- **年度報告**：財務或業績數據視覺化佔位
