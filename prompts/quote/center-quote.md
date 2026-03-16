---
layout: quote
name: 金句引言 / 客戶見證
tags: [quote, testimonial, pullquote, minimalist]
---

# 金句引言 / 客戶見證 Prompt 模版

## 版型預覽

```
+--------------------------------------------------+
| "  (超大引號，品牌色，左上角裝飾)                |
|                                                  |
|                                                  |
|       "{quote_text}"                             |
|       （置中，大字，加粗）                        |
|                                                  |
|                                                  |
|                      [頭像] {speaker_name}       |
|                             {speaker_title}      |
+--------------------------------------------------+
```
（大量留白，極簡風格；可切換深色/淺色背景模式）

## 適用情境

- 簡報中穿插有力引言，強化論點或情感共鳴
- 客戶見證頁，展示使用者的真實回饋
- 演講結尾用名人金句收尾，留下深刻印象

## Core Prompt

```
Create a 16:9 minimalist presentation slide for a pull quote or customer testimonial.

Style: Maximum white space. No decorative borders or busy elements. Let the quote breathe.

BACKGROUND: If {bg_mode} is "dark", fill the entire slide with {accent_color}. If "light", fill with #FFFFFF or #FAFAFA.
Text color adapts accordingly: dark mode → white (#FFFFFF); light mode → near-black (#1A1A1A).

LARGE QUOTATION MARK (decoration):
- Position: top-left area, approximately left=5%, top=5% of slide.
- Character: " (left double quotation mark, Unicode U+201C)
- Font size: 120pt, bold.
- Color: {accent_color} in light mode; rgba(255,255,255,0.25) (semi-transparent white) in dark mode.

QUOTE BODY:
- Text: "{quote_text}"
- Horizontal: centered, with left/right margins of ~15% each side.
- Vertical: centered on the slide (accounting for decoration and attribution).
- Font size: {quote_font_size}pt (recommended 28–34pt), bold.
- Color: as per bg_mode rules above.
- Line height: 1.5×.

ATTRIBUTION (bottom-right quadrant):
- Optional small circular avatar placeholder (diameter ~50pt) for {speaker_photo}
- Speaker name: "{speaker_name}", bold, font size 15pt.
- Speaker title / source: "{speaker_title}", regular weight, font size 13pt, slightly muted color.
- Stack name above title, positioned right-aligned approximately at 80% from left, 82% from top.
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{quote_text}` | 引言正文，建議 30–60 字 | `This platform cut our reporting time by 80%. It's the most impactful tool we've adopted this year.` |
| `{speaker_name}` | 說話者姓名 | `Sarah Lin` |
| `{speaker_title}` | 說話者職稱或來源 | `Head of Data, RetailCo` |
| `{speaker_photo}` | 小頭像圖片路徑（可選） | `assets/sarah-lin.jpg` |
| `{accent_color}` | 品牌色（引號裝飾 / 深色背景） | `#1E3A8A` |
| `{bg_mode}` | 背景模式：`dark` 或 `light` | `dark` |
| `{quote_font_size}` | 引言字級（pt） | `30` |

## python-pptx 程式碼骨架

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


def build_quote(slide, s: dict):
    """
    建立金句引言 / 客戶見證版型。
    s 需包含：quote_text, speaker_name, speaker_title,
              speaker_photo (可選), accent_color,
              bg_mode ("dark" | "light"), quote_font_size
    """
    SLIDE_W = Inches(13.33)
    SLIDE_H = Inches(7.5)

    bg_mode = s.get("bg_mode", "light")
    accent = RGBColor.from_string(s.get("accent_color", "1E3A8A").lstrip("#"))

    if bg_mode == "dark":
        bg_color = accent
        text_color = RGBColor(0xFF, 0xFF, 0xFF)
        quote_mark_color = RGBColor(0xAA, 0xBB, 0xDD)  # 半透明白近似
    else:
        bg_color = RGBColor(0xFF, 0xFF, 0xFF)
        text_color = RGBColor(0x1A, 0x1A, 0x1A)
        quote_mark_color = accent

    # ── 背景 ──────────────────────────────────────────────────
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H,
             fill_color=bg_color)

    # ── 超大引號裝飾（左上角） ────────────────────────────────
    add_text(
        slide, "\u201C",  # 左雙引號 "
        left=Inches(0.5), top=Inches(0.2),
        width=Inches(2.0), height=Inches(1.8),
        font_size=Pt(120), bold=True,
        color=quote_mark_color,
        align=PP_ALIGN.LEFT, font_name="Georgia"
    )

    # ── 引言正文（水平垂直置中） ──────────────────────────────
    margin_lr = SLIDE_W * 0.15
    add_text(
        slide, s.get("quote_text", ""),
        left=margin_lr, top=Inches(1.8),
        width=SLIDE_W - margin_lr * 2, height=Inches(4.0),
        font_size=Pt(s.get("quote_font_size", 30)),
        bold=True, color=text_color,
        align=PP_ALIGN.CENTER, font_name="Calibri"
    )

    # ── 署名區（右下角） ──────────────────────────────────────
    attrib_left = SLIDE_W * 0.6
    attrib_top = SLIDE_H - Inches(1.5)
    attrib_w = SLIDE_W * 0.35

    # 小頭像佔位（可選）
    photo_path = s.get("speaker_photo", "")
    avatar_size = Inches(0.6)
    if photo_path:
        # slide.shapes.add_picture(photo_path, attrib_left, attrib_top, avatar_size, avatar_size)
        add_rect(slide, attrib_left, attrib_top, avatar_size, avatar_size,
                 fill_color=RGBColor(0xAA, 0xAA, 0xAA))
        name_left = attrib_left + avatar_size + Inches(0.15)
    else:
        name_left = attrib_left

    # 姓名
    add_text(
        slide, s.get("speaker_name", ""),
        left=name_left, top=attrib_top,
        width=attrib_w, height=Inches(0.45),
        font_size=Pt(15), bold=True,
        color=text_color,
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )

    # 職稱 / 來源
    muted = RGBColor(0xBB, 0xBB, 0xBB) if bg_mode == "dark" else RGBColor(0x77, 0x77, 0x77)
    add_text(
        slide, s.get("speaker_title", ""),
        left=name_left, top=attrib_top + Inches(0.45),
        width=attrib_w, height=Inches(0.4),
        font_size=Pt(13), bold=False,
        color=muted,
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )
```

## 範例

### 輸入範例

SaaS 產品簡報，引用某電商平臺 Head of Data 的正面評價，搭配深色品牌背景：

```python
s = {
    "quote_text": "This platform cut our reporting time by 80%. It's the most impactful tool we've adopted this year.",
    "speaker_name": "Sarah Lin",
    "speaker_title": "Head of Data, RetailCo",
    "speaker_photo": "assets/sarah-lin.jpg",
    "accent_color": "#1E3A8A",
    "bg_mode": "dark",
    "quote_font_size": 30,
}
```

### 輸出效果

深藍色背景填滿整張投影片，左上角顯示淡藍色超大引號裝飾，中央白色大字引言置中顯示，右下角有小頭像佔位、白色姓名「Sarah Lin」及灰色職稱文字。整體極簡、震撼，適合插入簡報的關鍵轉折點。
