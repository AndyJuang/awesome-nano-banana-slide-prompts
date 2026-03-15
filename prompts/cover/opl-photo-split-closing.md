---
layout: cover
name: 結尾感謝頁（封面變體）
tags: [closing, thank-you, end-slide, cover-variant]
source: 曜捷_公司簡介_簡報草稿_20260310.pptx — Slide 15
---

# 結尾感謝頁 Prompt 模版

> 與「三欄照片切割封面」共用相同佈局，僅文字內容不同

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│ [Logo 左上角 — 9pt]                                          │
│ ┌──────────┐ ┌──────────┐ ┌─────────────────────────────┐  │
│ │          │ │          │ │  ████████████████████████   │  │
│ │  Photo 1 │ │  Photo 2 │ │  （品牌色塊 — 空白）          │  │
│ │          │ ├──────────┤ │                             │  │
│ │          │ │  Photo 3 │ │                             │  │
│ └──────────┘ └──────────┘ └─────────────────────────────┘  │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │  感謝您   50pt Bold                                      │ │
│ │  Thank you   22pt Bold                                  │ │
│ │                                         [ END ]         │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 與封面的差異對照

| 元素 | 封面（Slide 1） | 結尾（Slide 15） |
|------|----------------|----------------|
| 品牌色塊右側文字 | `{brand_name_line_1}` / `{brand_name_line_2}` 46pt | **無文字**（純色塊）|
| 主標題 | 公司名稱 38pt | `感謝您` **50pt** |
| 副標題 | 英文公司名 17pt | `Thank you` **22pt** |
| 按鈕文字 | `START` | `END` |
| 按鈕寬度 | 1.60" | **1.90"**（稍寬）|

## Core Prompt

```
Generate a closing/thank-you slide (16:9, 13.33" × 7.50"):

Use the same layout as the photo-split cover slide, with these modifications:

=== UPPER HALF (same photo grid + brand block) ===
[Identical structure to cover — see opl-photo-split-cover.md]

Brand block text: OMIT the brand name lines (leave the color block empty)
  Rectangle: x=6.50", y=0, width=6.83", height=4.50", fill={brand_color}
  No text overlaid on the brand block

=== LOWER HALF (closing content) ===
Bottom white area:
  Rectangle: x=0, y=4.55", full width, height=2.95", fill=white

Primary closing text:
  Text: "{closing_primary}" — 50pt, Bold, {closing_color}
  Position: x=0.80", y=4.65", width=11.70"
  Examples: "感謝您" / "Thank You" / "Q&A"

Secondary closing text:
  Text: "{closing_secondary}" — 22pt, Bold, {closing_color}
  Position: x=0.80", y=5.75", width=11.70"
  Examples: "Thank you" / "Questions?" / ""

End button:
  Rectangle: x=5.70", y=6.72", width=1.90", height=0.45", white fill, light border
  Label: "{end_button_text}" — 12pt, centered
  Default: "END"
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{brand_color}` | 右側品牌色塊 | `#1B4F9B` |
| `{brand_name_line_1}` | 品牌名第一行（封面用，結尾頁留空） | `{brand_name_line_1}` |
| `{brand_name_line_2}` | 品牌名第二行（封面用，結尾頁留空） | `{brand_name_line_2}` |
| `{closing_primary}` | 主要結尾文字 | `感謝您` / `Thank You` |
| `{closing_color}` | 結尾文字色 | `#404040` |
| `{closing_secondary}` | 次要結尾文字 | `Thank you` / `謝謝` |
| `{end_button_text}` | 結束按鈕文字 | `END` / `FIN` |

## python-pptx 程式碼骨架

```python
def build_closing_slide(prs, closing_primary="感謝您", closing_secondary="Thank you",
                         logo_text="BRAND", brand_color=None, image_paths=None):
    """
    結尾感謝頁（封面結構變體）
    直接呼叫 build_photo_split_cover 並覆寫相關參數
    """
    return build_photo_split_cover(
        prs,
        brand_name_1="",          # 品牌色塊不加文字
        brand_name_2="",
        main_title=closing_primary,
        subtitle=closing_secondary,
        logo_text=logo_text,
        cta_text="END",
        brand_color=brand_color,
        image_paths=image_paths,
        # 覆寫字號差異需在 build_photo_split_cover 加 title_font_size 參數
    )
    # 注意：closing_primary 字號為 50pt（vs 封面 38pt），
    # 需在 build_photo_split_cover 增加 title_font_size 可選參數
```
