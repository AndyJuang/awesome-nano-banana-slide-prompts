---
layout: big_title
tags: [big-title, statement, keynote, social-media]
updated: 2026-03-16
---

# Big Title — 震撼宣言頁 (Impact Statement)

## 版面規格

```
┌─────────────────────────────────────────────────┐
│ [brand_name]                                    │ ← 頂部細色條 + Logo
│                                                 │
│                                                 │
│         {main_title}                            │ ← 巨大主句，垂直置中
│         （60pt，粗體，畫面焦點）                  │
│                                                 │
│         {sub_text}                              │ ← 輔助說明（可省略）
│                                                 │
└─────────────────────────────────────────────────┘
```

**畫布尺寸：** 33.87 × 19.05 cm（16:9 寬螢幕）
**設計原則：** 極致留白，單一焦點，禁止超過 2 行主句

---

## Core Prompt

Create a **big title slide** with maximum visual impact. The layout should have generous white space, with the headline centered both horizontally and vertically.

**Visual Structure:**
- Background: solid `{bg_color}` (default: pure white `#FFFFFF`)
- Top edge: thin `{accent_color}` accent bar (≈ 0.08 inch tall)
- Top-left corner: `{logo_text}` in 9pt, brand color
- Center: `{main_title}` at `{title_size}`pt (default 60pt), bold, in `{text_color}`
- Below headline (if provided): `{sub_text}` at 24pt, muted grey, centered

**Typography:**
- Headline font: match brand typeface; fallback Microsoft JhengHei / Calibri
- Sub-text: same family, regular weight
- Maximum headline: 2 lines; single impactful statement preferred

---

## 變數說明

| 變數 | 說明 | 範例 |
|------|------|------|
| `{logo_text}` | 左上角品牌標識文字 | `MY BRAND` |
| `{main_title}` | 主句（1-2 行震撼宣言或單一大數據） | `全球 60+ 個國家，共同守護每一票貨` |
| `{sub_text}` | 輔助說明文字（可省略） | `自 2001 年深耕物流產業` |
| `{bg_color}` | 背景色（hex） | `#FFFFFF` |
| `{text_color}` | 主標題文字色 | `#1A1A1A` |
| `{accent_color}` | 頂部色條與 Logo 色 | `#1B4F9B` |
| `{title_size}` | 主標題字號（pt） | `60` |

---

## python-pptx 骨架

```python
{
  "layout": "big_title",
  "logo_text": "{logo_text}",
  "main_title": "{main_title}",
  "sub_text": "{sub_text}",
  "bg_color": "{bg_color}",
  "text_color": "{text_color}",
  "accent_color": "{accent_color}",
  "title_size": 60
}
```

---

## 適用情境

- **大型年度演講 / 簡報開場**：單一宣言破題，引發情緒共鳴
- **社群行銷懶人包**：手機閱讀友善，字少圖大的首頁
- **章節轉換強調**：強烈單一數據或痛點呈現
