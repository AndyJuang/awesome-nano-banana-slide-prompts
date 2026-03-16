---
layout: image_gallery
name: 多圖畫廊 / 四格拼貼
tags: [image-gallery, mosaic, photo-grid, multi-image]
---

# 多圖畫廊 / 四格拼貼 Prompt 模版

## 版型預覽

```
+--------------------------------------------------+
|  {slide_title}                                   |
+------------------------+-------------------------+
|                        |                         |
|      [IMAGE 1]         |      [IMAGE 2]          |
|                        |                         |
|████ {caption_1} ██████|████ {caption_2} █████████|
+------------------------+-------------------------+
|                        |                         |
|      [IMAGE 3]         |      [IMAGE 4]          |
|                        |                         |
|████ {caption_3} ██████|████ {caption_4} █████████|
+------------------------+-------------------------+
```
（每格圖片全出血填滿格子，底部半透明深色條疊加白色圖說文字）

## 適用情境

- 產品功能展示，同時呈現多個介面截圖或使用情境照片
- 活動回顧或案例集錦，用視覺拼貼方式呈現多張精選照片
- 比較不同方案或版本，並附上簡短圖說說明差異

## Core Prompt

```
Create a 16:9 presentation slide with a 2×2 photo mosaic grid layout.

Slide structure:
- TOP BAR (height: ~12% of slide): Display "{slide_title}" as the slide title, left-aligned, font size {title_font_size}pt, bold, color {accent_color}. White or light background for the title bar.
- GRID (remaining ~88%): Divide evenly into 4 equal cells (2 columns × 2 rows).
  - Cell 1 (top-left): Full-bleed image placeholder using {img_path_1}
  - Cell 2 (top-right): Full-bleed image placeholder using {img_path_2}
  - Cell 3 (bottom-left): Full-bleed image placeholder using {img_path_3}
  - Cell 4 (bottom-right): Full-bleed image placeholder using {img_path_4}
- CAPTION BAR (per cell, bottom 18% of each cell): Semi-transparent dark overlay (#000000 at 60% opacity) across the full cell width. White caption text "{caption_N}" centered vertically in the bar, font size {caption_font_size}pt, regular weight.

Style: Modern, clean. Thin white 2pt separator lines between grid cells. No outer border on cells.
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{slide_title}` | 投影片頂部標題文字 | `New Feature Overview` |
| `{img_path_1}` | 第 1 張圖片的檔案路徑 | `assets/feature-dashboard.png` |
| `{img_path_2}` | 第 2 張圖片的檔案路徑 | `assets/feature-reports.png` |
| `{img_path_3}` | 第 3 張圖片的檔案路徑 | `assets/feature-mobile.png` |
| `{img_path_4}` | 第 4 張圖片的檔案路徑 | `assets/feature-api.png` |
| `{caption_1}` | 第 1 張圖片的圖說文字 | `即時儀表板` |
| `{caption_2}` | 第 2 張圖片的圖說文字 | `智慧報表` |
| `{caption_3}` | 第 3 張圖片的圖說文字 | `行動端體驗` |
| `{caption_4}` | 第 4 張圖片的圖說文字 | `開放 API 整合` |
| `{accent_color}` | 品牌主色（用於標題文字） | `#1A73E8` |
| `{title_font_size}` | 標題字級（pt） | `32` |
| `{caption_font_size}` | 圖說字級（pt） | `12` |

## python-pptx 程式碼骨架

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


def build_image_gallery(slide, s: dict):
    """
    建立 2×2 四格拼貼圖片畫廊版型。
    s 需包含：slide_title, img_path_1~4, caption_1~4,
              accent_color (hex str), title_font_size, caption_font_size
    """
    SLIDE_W = Inches(13.33)
    SLIDE_H = Inches(7.5)

    TITLE_H = Inches(0.9)
    GRID_TOP = TITLE_H
    GRID_H = SLIDE_H - TITLE_H
    CELL_W = SLIDE_W / 2
    CELL_H = GRID_H / 2
    CAP_H = CELL_H * 0.18  # 圖說條高度為格子高度的 18%

    accent = RGBColor.from_string(s.get("accent_color", "1A73E8").lstrip("#"))

    # ── 標題列背景 ──────────────────────────────────────────
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, TITLE_H,
             fill_color=RGBColor(0xFF, 0xFF, 0xFF))

    # ── 標題文字 ─────────────────────────────────────────────
    add_text(
        slide, s.get("slide_title", ""),
        left=Inches(0.3), top=Inches(0), width=SLIDE_W - Inches(0.6), height=TITLE_H,
        font_size=Pt(s.get("title_font_size", 32)),
        bold=True, color=accent,
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )

    # ── 四格圖片與圖說 ────────────────────────────────────────
    cells = [
        (0, 0, "img_path_1", "caption_1"),
        (1, 0, "img_path_2", "caption_2"),
        (0, 1, "img_path_3", "caption_3"),
        (1, 1, "img_path_4", "caption_4"),
    ]

    for col, row, img_key, cap_key in cells:
        cell_left = CELL_W * col
        cell_top = GRID_TOP + CELL_H * row

        # 圖片佔位（灰底，代表全出血圖片）
        add_rect(slide, cell_left, cell_top, CELL_W, CELL_H,
                 fill_color=RGBColor(0xCC, 0xCC, 0xCC))

        # 若有實際圖片路徑，可在此插入 slide.shapes.add_picture(...)

        # 白色格線（簡單用白框矩形模擬）
        add_rect(slide, cell_left, cell_top, CELL_W, CELL_H,
                 fill_color=None,
                 border_color=RGBColor(0xFF, 0xFF, 0xFF))

        # 圖說半透明深色底條（python-pptx 不原生支援透明度，用深灰近似）
        cap_top = cell_top + CELL_H - CAP_H
        add_rect(slide, cell_left, cap_top, CELL_W, CAP_H,
                 fill_color=RGBColor(0x20, 0x20, 0x20))

        # 圖說文字
        add_text(
            slide, s.get(cap_key, ""),
            left=cell_left + Inches(0.1), top=cap_top,
            width=CELL_W - Inches(0.2), height=CAP_H,
            font_size=Pt(s.get("caption_font_size", 12)),
            bold=False, color=RGBColor(0xFF, 0xFF, 0xFF),
            align=PP_ALIGN.LEFT, font_name="Calibri"
        )
```

## 範例

### 輸入範例

產品發布簡報中，展示新版 SaaS 平臺的四個核心功能介面截圖：

```python
s = {
    "slide_title": "New Feature Overview",
    "img_path_1": "assets/feature-dashboard.png",
    "img_path_2": "assets/feature-reports.png",
    "img_path_3": "assets/feature-mobile.png",
    "img_path_4": "assets/feature-api.png",
    "caption_1": "即時儀表板",
    "caption_2": "智慧報表",
    "caption_3": "行動端體驗",
    "caption_4": "開放 API 整合",
    "accent_color": "#1A73E8",
    "title_font_size": 32,
    "caption_font_size": 12,
}
```

### 輸出效果

投影片頂部顯示藍色標題「New Feature Overview」，下方四格各填入不同介面截圖（灰底佔位）。每格底部有深色圖說條加上白色圖說文字，格與格之間有白色細線分隔，整體感覺現代、乾淨，適合技術或產品發布簡報。
