---
layout: left-img-right-points
name: 左圖右重點
tags: [image, key-points, split-layout, photo]
---

# 左圖右重點 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO]                                    ■ ■ □            │
│  ■ 標題文字（Title）                                         │
│  ───────────────────────────────────                        │
│                                                              │
│  ┌──────────────────────────┐  ┌───────────────────────┐   │
│  │                          │  │  ● 重點一              │   │
│  │                          │  │    說明文字            │   │
│  │     主視覺圖片            │  │                        │   │
│  │    (50–55% 寬)           │  │  ● 重點二              │   │
│  │                          │  │    說明文字            │   │
│  │                          │  │                        │   │
│  │  [圖片說明]               │  │  ● 重點三              │   │
│  └──────────────────────────┘  └───────────────────────┘   │
│  ─────────────────────────────────────────── 底部裝飾線     │
└─────────────────────────────────────────────────────────────┘
```

## 適用場景

- 展示產品/場地照片 + 旁邊條列特色
- 案例分享：左側案例圖，右側成果重點
- 服務介紹：左側服務現場，右側服務項目

## Core Prompt

```
Generate a left-image-right-keypoints slide (16:9):

Title bar (top, full width):
  - Small accent marker (colored square or icon) before title
  - Title text: "{title}"
  - Thin horizontal rule below title
  - Decorative elements at top-right: 2–3 colored squares of varying sizes

Left panel ({left_ratio}% of slide width, vertically centered):
  - Image: "{image_description}"
  - Image style: {image_style}
    Options: "full-bleed fills panel" | "with drop shadow and rounded corners" | "with border"
  - Caption below image: "{image_caption}" (omit if not needed)
  - Caption style: small, muted color, centered under image

Right panel ({right_ratio}% of slide width, vertically centered):
  Key points — use {bullet_style} bullet style:
    Options: "filled colored circle" | "numbered badge" | "arrow" | "dash"

  Point 1: "{point_1_heading}"
    Description: "{point_1_body}"

  Point 2: "{point_2_heading}"
    Description: "{point_2_body}"

  Point 3: "{point_3_heading}"
    Description: "{point_3_body}"

  (optional) Point 4: "{point_4_heading}"
    Description: "{point_4_body}"

Divider between panels:
  {divider_style}
  Options: "none" | "1px vertical line in muted gray" | "8px gap with subtle shadow"

Bottom decoration:
  {bottom_style}
  Options: "thin full-width accent line" | "none"

Color scheme:
  Background: {bg_color}
  Title accent: {accent_color}
  Bullet/icon color: {bullet_color}
  Body text: {text_color}
  Caption: muted, 70% opacity of body text color
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{title}` | 投影片主標題 | `Our Warehouse Network` |
| `{left_ratio}` | 左側圖片佔寬比例（%） | `52` |
| `{right_ratio}` | 右側重點佔寬比例（%） | `44` |
| `{image_description}` | 圖片內容描述 | `aerial view of modern logistics warehouse` |
| `{image_style}` | 圖片顯示樣式 | `full-bleed fills panel` |
| `{image_caption}` | 圖片說明文字 | `Taichung Distribution Center, 45,000 m²` |
| `{bullet_style}` | 項目符號樣式 | `filled colored circle` |
| `{point_N_heading}` | 第 N 個重點標題 | `24/7 Operations` |
| `{point_N_body}` | 第 N 個重點說明 | `Round-the-clock monitoring and dispatch` |
| `{divider_style}` | 左右分隔方式 | `1px vertical line in muted gray` |
| `{bg_color}` | 背景顏色 | `white` 或 `#F8F9FA` |
| `{accent_color}` | 標題強調色 | `#0091D5` |
| `{bullet_color}` | 項目符號顏色 | `#1B4F9B` |
| `{text_color}` | 正文顏色 | `#404040` |

## 版型細節規範

### 版面配置
- 標題列：距頂 5–8%，高度約 12%
- 左圖：從標題下方到底部裝飾線，留 3% 上下 padding
- 右側重點：垂直居中，留 4% 內縮，項目間距均等
- 最多建議 4 個重點（超過請拆成兩頁）

### 圖片比例注意
- 左側 panel 約 6:7 比例（接近直幅），圖片需裁切配合
- 若原圖為橫幅，考慮改用「上圖下文」版型

### 色彩建議
- 背景：白色或極淺灰（讓圖片成為視覺焦點）
- 項目符號：使用品牌強調色（增加辨識感）
- 重點標題：加粗，與說明文字形成層次

## python-pptx 程式碼骨架

```python
def build_left_img_right_points_slide(prs, title, image_path, points,
                                       accent_color, left_ratio=0.52):
    """
    建立左圖右重點投影片

    Args:
        prs: Presentation 物件
        title: 標題文字 (str)
        image_path: 圖片路徑 (str)，None 時用色塊佔位
        points: 重點清單 [{"heading": str, "body": str}, ...]，最多4項
        accent_color: RGBColor，強調色
        left_ratio: 左側圖片寬度比例，預設 0.52
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    W, H = prs.slide_width, prs.slide_height

    PADDING = Inches(0.3)
    TITLE_HEIGHT = Inches(0.8)
    TITLE_TOP = Inches(0.5)

    # 標題左側色塊裝飾
    add_rect(slide, PADDING, TITLE_TOP + Inches(0.1),
             Inches(0.15), Inches(0.5), fill_color=accent_color)

    # 標題文字
    add_text_box(slide, title,
                 PADDING + Inches(0.25), TITLE_TOP,
                 W - Inches(2), TITLE_HEIGHT,
                 font_size=24, bold=True, color=RGBColor(40, 40, 40))

    # 標題下方分隔線
    add_rect(slide, PADDING, TITLE_TOP + TITLE_HEIGHT + Inches(0.05),
             W - PADDING * 2, Inches(0.02), fill_color=accent_color)

    # 左側圖片區
    img_left = PADDING
    img_top = TITLE_TOP + TITLE_HEIGHT + Inches(0.2)
    img_width = W * left_ratio - PADDING
    img_height = H - img_top - Inches(0.4)

    if image_path:
        slide.shapes.add_picture(image_path, img_left, img_top,
                                 img_width, img_height)
    else:
        add_rect(slide, img_left, img_top, img_width, img_height,
                 fill_color=RGBColor(180, 190, 200))

    # 右側重點區
    rp_left = W * left_ratio + Inches(0.1)
    rp_width = W - rp_left - PADDING
    rp_top = img_top
    item_height = img_height / max(len(points), 1)

    for i, point in enumerate(points[:4]):
        y = rp_top + item_height * i

        # 項目符號圓點
        dot_size = Inches(0.18)
        add_rect(slide, rp_left, y + item_height * 0.2,
                 dot_size, dot_size, fill_color=accent_color)

        # 重點標題
        add_text_box(slide, point.get("heading", ""),
                     rp_left + dot_size + Inches(0.1), y,
                     rp_width - dot_size - Inches(0.1), item_height * 0.4,
                     font_size=16, bold=True, color=RGBColor(40, 40, 40))

        # 重點說明
        if point.get("body"):
            add_text_box(slide, point["body"],
                         rp_left + dot_size + Inches(0.1),
                         y + item_height * 0.4,
                         rp_width - dot_size - Inches(0.1), item_height * 0.5,
                         font_size=13, color=RGBColor(100, 100, 100))

    return slide
```

## 範例

### 輸入範例
「左側放台中倉儲中心的照片，右側列出三個重點：24小時營運、自動化分揀、即時庫存追蹤」

### 輸出效果
左側 52% 為倉儲照片，右側 44% 三個圓點重點條列，
標題「台中物流中心」帶藍色標記，底部細線收尾
