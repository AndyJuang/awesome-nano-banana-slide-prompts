---
layout: cover
name: 基礎封面頁
tags: [cover, opening, brand]
---

# 基礎封面頁 Prompt 模版

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO]                                                       │
│                                                              │
│  ┌────────────────────────┐  ┌──────────────────────────┐   │
│  │                        │  │                          │   │
│  │    Hero Image / Visual │  │  ██ Brand Color Block ██ │   │
│  │         (60%)          │  │     Brand Name (40%)     │   │
│  │                        │  │                          │   │
│  └────────────────────────┘  └──────────────────────────┘   │
│                                                              │
│         MAIN TITLE — 主標題（大、置中或左對齊）               │
│         Subtitle / Tagline — 副標題（較小）                  │
│                                          [CTA Button / Date] │
└─────────────────────────────────────────────────────────────┘
```

## 適用場景

- 簡報開場第一頁
- 品牌或公司介紹的首頁
- 活動、發表會封面

## Core Prompt

```
Generate a cover slide with the following layout (16:9, 1920×1080px):

Background: {background_style}
  Options: "split — left 60% hero image, right 40% dark brand color block"
           "full-bleed image with overlay"
           "clean white with geometric accent"

Logo: place {logo_description} at {logo_position}
  Options for position: "top-left" | "top-right" | "bottom-right"

Main title: "{main_title}"
  Style: {title_size}pt, bold, color={title_color}
  Position: {title_position}
  Options for position: "lower-left" | "center" | "lower-center"

Subtitle / Tagline: "{subtitle}"
  Style: {subtitle_size}pt, normal weight, color={subtitle_color}
  Position: directly below main title

Visual element: {visual_description}
  This is the hero image or graphic occupying the left/top portion

Bottom area:
  {bottom_left}: "{presenter_or_date}"
  {bottom_right}: "{event_or_version}"

Color palette:
  Primary: {primary_color}
  Accent: {accent_color}
  Text on dark: white
  Text on light: {dark_text_color}
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{background_style}` | 背景設計方式 | `split — left 60% hero image, right 40% navy block` |
| `{logo_description}` | LOGO 描述或名稱 | `company wordmark in white` |
| `{logo_position}` | LOGO 位置 | `top-left` |
| `{main_title}` | 主標題文字 | `2026 Company Overview` |
| `{title_size}` | 主標題字號 | `48` |
| `{title_color}` | 主標題顏色 | `#FFFFFF` 或 `navy blue` |
| `{title_position}` | 標題位置 | `lower-left, 10% from bottom` |
| `{subtitle}` | 副標題或 tagline | `Powering Tomorrow's Logistics` |
| `{subtitle_size}` | 副標題字號 | `24` |
| `{subtitle_color}` | 副標題顏色 | `#E0E0E0` |
| `{visual_description}` | 主視覺描述 | `aerial view of container port` |
| `{primary_color}` | 主品牌色 | `#1B4F9B` |
| `{accent_color}` | 強調色 | `#0091D5` |
| `{dark_text_color}` | 深色文字顏色 | `#404040` |

## 版型細節規範

### 版面配置
- 視覺區：左側 55–65%，全高
- 品牌色塊：右側 35–45%，全高
- 標題區：下半部（距底部 15–25%）
- 頂部 LOGO：距邊緣 2–3% padding

### 色彩建議
- 深色背景塊配白色文字
- 避免在照片上直接放小字（需半透明遮罩）

### 字型規範
- 主標題：40–56pt，Bold
- 副標題：20–28pt，Regular 或 Light
- 公司名/LOGO：14–18pt，Bold

## python-pptx 程式碼骨架

```python
def build_cover_slide(prs, main_title, subtitle, brand_color, accent_color,
                      logo_text="BRAND", bg_image_path=None):
    """
    建立封面投影片

    Args:
        prs: Presentation 物件
        main_title: 主標題文字
        subtitle: 副標題文字
        brand_color: RGBColor，主品牌色（深色塊用）
        accent_color: RGBColor，強調色
        logo_text: LOGO 替代文字
        bg_image_path: 左側英雄圖片路徑（可選）
    """
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    W, H = prs.slide_width, prs.slide_height

    # 右側品牌色塊（40% 寬）
    split = W * 0.6
    add_rect(slide, split, 0, W - split, H, fill_color=brand_color)

    # 左側英雄圖（或佔位色塊）
    if bg_image_path:
        slide.shapes.add_picture(bg_image_path, 0, 0, split, H)
    else:
        add_rect(slide, 0, 0, split, H, fill_color=RGBColor(80, 80, 90))

    # LOGO 文字（左上）
    add_text_box(slide, logo_text, Inches(0.3), Inches(0.2),
                 Inches(3), Inches(0.5), font_size=14, bold=True,
                 color=RGBColor(255, 255, 255))

    # 右側品牌名（色塊上方）
    add_text_box(slide, logo_text.upper(), split + Inches(0.3), Inches(1.5),
                 W - split - Inches(0.3), Inches(1),
                 font_size=18, bold=True, color=RGBColor(255, 255, 255))

    # 主標題（下半部）
    add_text_box(slide, main_title, Inches(0.5), H * 0.55,
                 W * 0.85, Inches(1.8), font_size=40, bold=True,
                 color=RGBColor(255, 255, 255))

    # 副標題
    add_text_box(slide, subtitle, Inches(0.5), H * 0.72,
                 W * 0.85, Inches(0.8), font_size=22,
                 color=RGBColor(200, 220, 240))

    return slide
```

## 範例

### 輸入範例
「封面：{品牌名稱}簡介，主標題『{品牌特色}』，副標題英文 {品牌名稱} ，右側深海軍藍色塊」

### 輸出效果
左側 60% 為貨輪/倉儲照片，右側 40% 深藍色塊帶白色 {品牌名稱} 字樣，
下方大白字「物流」，副標題灰白「{品牌縮寫} · {品牌名稱}」
