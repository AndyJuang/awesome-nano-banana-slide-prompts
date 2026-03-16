---
layout: video_demo
name: 影片 / Demo 展示頁
tags: [video, demo, mockup, laptop, product]
---

# 影片 / Demo 展示頁 Prompt 模版

## 版型預覽

```
+--------------------------------------------------+
|  {slide_title}                                   |
|                                                  |
|        +====================================+    |
|        |  +------------------------------ + |    |
|        |  |                              | |    |
|        |  |          ▶  PLAY             | |    |
|        |  |    (螢幕 16:9 影片佔位)       | |    |
|        |  +------------------------------+ |    |
|        |  [=====鍵盤底條===============]   |    |
|        +====================================+    |
|                                                  |
|  {cta_text}                                      |
+--------------------------------------------------+
```
（筆記型電腦外框：深灰矩形；螢幕：黑色矩形；鍵盤底條：中灰矩形；播放鍵：白色三角文字）

## 適用情境

- 產品 Demo 簡報，展示軟體介面或操作流程
- 影片行銷素材，嵌入影片連結並搭配說明文字
- 技術展示頁，以視覺化方式預告影片內容或操作截圖

## Core Prompt

```
Create a 16:9 presentation slide for a video or product demo showcase, featuring a laptop mockup built from rectangles.

SLIDE BACKGROUND: #FFFFFF white or very light gray #F8F8F8.

TOP TITLE:
- "{slide_title}" — single line, font size 28pt, bold, color #1A1A1A, left-aligned, top margin 5%.

LAPTOP MOCKUP (center of slide, built entirely from rectangles):
- OUTER BODY (laptop lid): A dark gray rectangle (#333333), width = 60% of slide width, height = 42% of slide height. Horizontally centered. Top edge at ~18% from top of slide.
  - Corner radius: simulate with a slightly lighter border or just use a plain rectangle.
- SCREEN AREA (inside lid): A black rectangle (#000000), inset ~4% from each side of the outer body, inset ~5% from top, leaving ~8% gap at bottom of lid for bezel.
- PLAY ICON (inside screen): Centered in the screen area. A white right-pointing triangle character "▶" at 48pt, followed by a subtitle line "Watch Demo" in white, 14pt, regular weight. Both lines center-aligned vertically and horizontally within the screen.
- KEYBOARD BASE: A medium gray rectangle (#555555), width = 65% of slide width (slightly wider than lid), height = 5% of slide height. Top edge touching the bottom edge of the laptop lid. Horizontally centered.

BOTTOM CTA TEXT (optional):
- "{cta_text}" — centered, font size 16pt, color #555555, italic, positioned at bottom 10% of slide.
- If {cta_text} is empty, omit this element.

No additional decorative elements. Keep it clean and focused on the mockup.
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 頂部短標題（一行以內） | `See It in Action` |
| `{video_url}` | 影片連結（資料記錄用，pptx 中以佔位呈現） | `https://youtu.be/abc123` |
| `{cta_text}` | 底部行動呼籲文字（可選，留空則不顯示） | `Watch Full Demo →` |
| `{laptop_color}` | 筆記型電腦外框顏色 | `#333333` |
| `{screen_color}` | 螢幕底色 | `#000000` |
| `{play_icon_color}` | 播放鍵顏色 | `#FFFFFF` |

## python-pptx 程式碼骨架

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


def build_video_demo(slide, s: dict):
    """
    建立影片 / Demo 展示頁版型（筆記型電腦 Mockup）。
    s 需包含：slide_title, video_url (可選), cta_text (可選),
              laptop_color, screen_color, play_icon_color
    """
    SLIDE_W = Inches(13.33)
    SLIDE_H = Inches(7.5)

    def hex_to_rgb(h):
        h = h.lstrip("#")
        return RGBColor.from_string(h)

    laptop_color = hex_to_rgb(s.get("laptop_color", "#333333"))
    screen_color = hex_to_rgb(s.get("screen_color", "#000000"))
    play_color   = hex_to_rgb(s.get("play_icon_color", "#FFFFFF"))
    kbd_color    = RGBColor(0x55, 0x55, 0x55)

    # ── 背景 ──────────────────────────────────────────────────
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H,
             fill_color=RGBColor(0xF8, 0xF8, 0xF8))

    # ── 頂部標題 ──────────────────────────────────────────────
    add_text(
        slide, s.get("slide_title", ""),
        left=Inches(0.6), top=Inches(0.35),
        width=SLIDE_W - Inches(1.2), height=Inches(0.65),
        font_size=Pt(28), bold=True,
        color=RGBColor(0x1A, 0x1A, 0x1A),
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )

    # ── 筆記型電腦 Mockup ─────────────────────────────────────
    # 外框（螢幕蓋）尺寸
    lid_w = SLIDE_W * 0.60
    lid_h = SLIDE_H * 0.42
    lid_left = (SLIDE_W - lid_w) / 2
    lid_top = SLIDE_H * 0.18

    # 外框深灰矩形
    add_rect(slide, lid_left, lid_top, lid_w, lid_h,
             fill_color=laptop_color)

    # 螢幕黑色矩形（內縮）
    bezel = Inches(0.18)
    scr_left = lid_left + bezel
    scr_top  = lid_top + bezel
    scr_w    = lid_w - bezel * 2
    scr_h    = lid_h - bezel * 2.5  # 底部留較多邊框
    add_rect(slide, scr_left, scr_top, scr_w, scr_h,
             fill_color=screen_color)

    # 播放鍵 ▶（螢幕中央）
    add_text(
        slide, "▶",
        left=scr_left, top=scr_top,
        width=scr_w, height=scr_h * 0.6,
        font_size=Pt(48), bold=False,
        color=play_color,
        align=PP_ALIGN.CENTER, font_name="Segoe UI Symbol"
    )

    # 播放說明文字
    add_text(
        slide, "Watch Demo",
        left=scr_left, top=scr_top + scr_h * 0.55,
        width=scr_w, height=scr_h * 0.3,
        font_size=Pt(14), bold=False,
        color=play_color,
        align=PP_ALIGN.CENTER, font_name="Calibri"
    )

    # 鍵盤底條
    kbd_w = SLIDE_W * 0.65
    kbd_h = SLIDE_H * 0.05
    kbd_left = (SLIDE_W - kbd_w) / 2
    kbd_top  = lid_top + lid_h
    add_rect(slide, kbd_left, kbd_top, kbd_w, kbd_h,
             fill_color=kbd_color)

    # ── 底部 CTA 文字（可選） ──────────────────────────────────
    cta = s.get("cta_text", "")
    if cta:
        add_text(
            slide, cta,
            left=Inches(0), top=SLIDE_H - Inches(0.75),
            width=SLIDE_W, height=Inches(0.6),
            font_size=Pt(16), bold=False,
            color=RGBColor(0x55, 0x55, 0x55),
            align=PP_ALIGN.CENTER, font_name="Calibri"
        )
```

## 範例

### 輸入範例

新產品發布會，展示 App 操作 Demo 影片，附上行動呼籲文字：

```python
s = {
    "slide_title": "See It in Action",
    "video_url": "https://youtu.be/abc123",
    "cta_text": "Watch Full Demo →",
    "laptop_color": "#333333",
    "screen_color": "#000000",
    "play_icon_color": "#FFFFFF",
}
```

### 輸出效果

淺灰色背景，頂部顯示深色粗體標題「See It in Action」。中央有擬真筆記型電腦外框（深灰矩形），螢幕區域填黑，中央顯示白色三角播放鍵「▶」及「Watch Demo」說明文字，底部有灰色鍵盤底條。最底部顯示灰色行動呼籲文字「Watch Full Demo →」。整體科技感強，重點突出。
