---
layout: speaker_profile
name: 講者 / 團隊成員介紹
tags: [speaker, profile, team, bio, intro]
---

# 講者 / 團隊成員介紹 Prompt 模版

## 版型預覽

```
+------------------+--------------------------------------+
|                  | ─────────────────────────────────── |
|   [  PHOTO  ]    |  ■ {expertise_1}                    |
|   (圓形頭像)     |  ■ {expertise_2}                    |
|                  |  ■ {expertise_3}                    |
|  {speaker_name}  |  ■ {expertise_4}  (可選)            |
|  {speaker_title} |                                     |
|                  |  [LinkedIn]  [Twitter]  [Email]      |
|   (左側 40%)     |           (右側 60%)                 |
+------------------+--------------------------------------+
```
（背景淺灰或白色；右側頂部有品牌色裝飾線；左側頭像可為圓形或矩形）

## 適用情境

- 研討會或課程開場，介紹主講者背景與專業領域
- 公司簡報中呈現核心團隊成員，建立信任感
- 活動手冊轉製投影片，需要完整個人簡介頁

## Core Prompt

```
Create a 16:9 presentation slide for a speaker or team member profile.

Layout: Two-column split. Left column = 40% of slide width. Right column = 60%.

LEFT COLUMN:
- Large circular (or rounded-rectangle) photo placeholder for {speaker_photo}, centered horizontally in the column, occupying roughly the top 65% of the column height.
- Below the photo: "{speaker_name}" in large bold text, font size {name_font_size}pt, color {accent_color}, center-aligned.
- Below the name: "{speaker_title}" in regular weight, font size {title_font_size}pt, color #666666, center-aligned.

RIGHT COLUMN:
- TOP DECORATION: A horizontal rule line in {accent_color}, 3pt thick, spanning 85% of the right column width, positioned at the top.
- EXPERTISE LIST: 3–5 bullet items. Each item consists of:
  - A small filled square (■) in {accent_color}, approximately 10×10pt
  - Followed by the expertise description text, font size {expertise_font_size}pt, color #333333
  - Items: "{expertise_1}", "{expertise_2}", "{expertise_3}", "{expertise_4}" (optional), "{expertise_5}" (optional)
- SOCIAL LINKS ROW (optional, bottom of right column): Icon placeholder boxes for LinkedIn, Twitter/X, and Email, each followed by the respective URL or handle in small text, font size 11pt.

Background: {bg_color} (recommended: #F5F5F5 light gray or #FFFFFF white).
Vertical divider: Optional thin line in {accent_color} between the two columns.
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{speaker_name}` | 講者姓名（大字顯示） | `Dr. Jane Chen` |
| `{speaker_title}` | 職稱或頭銜 | `CTO, TechCorp Inc.` |
| `{speaker_photo}` | 頭像圖片路徑 | `assets/speaker-jane.jpg` |
| `{expertise_1}` | 核心專長第 1 項 | `機器學習與 AI 應用` |
| `{expertise_2}` | 核心專長第 2 項 | `雲端架構設計` |
| `{expertise_3}` | 核心專長第 3 項 | `產品策略與 GTM` |
| `{expertise_4}` | 核心專長第 4 項（可選） | `開源社群貢獻` |
| `{expertise_5}` | 核心專長第 5 項（可選） | `（留空則不顯示）` |
| `{linkedin_url}` | LinkedIn 個人頁連結（可選） | `linkedin.com/in/janec` |
| `{twitter_url}` | Twitter/X 帳號（可選） | `@janec_ai` |
| `{email}` | 聯絡電子郵件（可選） | `jane@techcorp.com` |
| `{accent_color}` | 品牌色（裝飾線、方塊） | `#2563EB` |
| `{bg_color}` | 背景色 | `#F5F5F5` |
| `{name_font_size}` | 姓名字級（pt） | `28` |
| `{title_font_size}` | 職稱字級（pt） | `16` |
| `{expertise_font_size}` | 專長條目字級（pt） | `15` |

## python-pptx 程式碼骨架

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


def build_speaker_profile(slide, s: dict):
    """
    建立講者 / 團隊成員介紹版型。
    s 需包含：speaker_name, speaker_title, speaker_photo,
              expertise_1~5 (expertise_4/5 可選),
              linkedin_url, twitter_url, email (均可選),
              accent_color, bg_color,
              name_font_size, title_font_size, expertise_font_size
    """
    SLIDE_W = Inches(13.33)
    SLIDE_H = Inches(7.5)

    LEFT_W = SLIDE_W * 0.4
    RIGHT_W = SLIDE_W * 0.6
    RIGHT_LEFT = LEFT_W
    PADDING = Inches(0.4)

    accent = RGBColor.from_string(s.get("accent_color", "2563EB").lstrip("#"))
    bg_hex = s.get("bg_color", "F5F5F5").lstrip("#")
    bg_color = RGBColor.from_string(bg_hex)

    # ── 背景 ──────────────────────────────────────────────────
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H,
             fill_color=bg_color)

    # ── 左側：頭像佔位（圓角矩形近似圓形） ───────────────────
    photo_size = Inches(3.2)
    photo_left = (LEFT_W - photo_size) / 2
    photo_top = Inches(0.8)
    add_rect(slide, photo_left, photo_top, photo_size, photo_size,
             fill_color=RGBColor(0xCC, 0xCC, 0xCC))
    # 若有實際圖片：slide.shapes.add_picture(s["speaker_photo"], photo_left, photo_top, photo_size, photo_size)

    # ── 左側：姓名 ────────────────────────────────────────────
    name_top = photo_top + photo_size + Inches(0.25)
    add_text(
        slide, s.get("speaker_name", ""),
        left=Inches(0.1), top=name_top, width=LEFT_W - Inches(0.2), height=Inches(0.55),
        font_size=Pt(s.get("name_font_size", 28)),
        bold=True, color=accent,
        align=PP_ALIGN.CENTER, font_name="Calibri"
    )

    # ── 左側：職稱 ────────────────────────────────────────────
    title_top = name_top + Inches(0.55)
    add_text(
        slide, s.get("speaker_title", ""),
        left=Inches(0.1), top=title_top, width=LEFT_W - Inches(0.2), height=Inches(0.4),
        font_size=Pt(s.get("title_font_size", 16)),
        bold=False, color=RGBColor(0x66, 0x66, 0x66),
        align=PP_ALIGN.CENTER, font_name="Calibri"
    )

    # ── 右側：頂部裝飾線 ──────────────────────────────────────
    add_rect(slide, RIGHT_LEFT + PADDING, Inches(0.6),
             RIGHT_W - PADDING * 2, Inches(0.05),
             fill_color=accent)

    # ── 右側：核心專長條目 ────────────────────────────────────
    expertise_keys = ["expertise_1", "expertise_2", "expertise_3",
                      "expertise_4", "expertise_5"]
    exp_top = Inches(1.0)
    exp_h = Inches(0.75)
    bullet_size = Inches(0.18)

    for key in expertise_keys:
        text = s.get(key, "")
        if not text:
            continue
        # 品牌色小方塊
        add_rect(slide, RIGHT_LEFT + PADDING, exp_top + (exp_h - bullet_size) / 2,
                 bullet_size, bullet_size, fill_color=accent)
        # 專長文字
        add_text(
            slide, text,
            left=RIGHT_LEFT + PADDING + bullet_size + Inches(0.15),
            top=exp_top, width=RIGHT_W - PADDING * 2 - bullet_size - Inches(0.15),
            height=exp_h,
            font_size=Pt(s.get("expertise_font_size", 15)),
            bold=False, color=RGBColor(0x33, 0x33, 0x33),
            align=PP_ALIGN.LEFT, font_name="Calibri"
        )
        exp_top += exp_h

    # ── 右側：社群連結列（可選） ──────────────────────────────
    social_top = SLIDE_H - Inches(1.0)
    social_left = RIGHT_LEFT + PADDING
    icon_size = Inches(0.3)
    icon_gap = Inches(2.2)

    for i, (key, label) in enumerate([("linkedin_url", "LinkedIn"),
                                       ("twitter_url", "Twitter"),
                                       ("email", "Email")]):
        val = s.get(key, "")
        if not val:
            continue
        ix = social_left + i * icon_gap
        add_rect(slide, ix, social_top, icon_size, icon_size,
                 fill_color=accent)
        add_text(
            slide, val,
            left=ix + icon_size + Inches(0.08), top=social_top,
            width=Inches(1.8), height=icon_size,
            font_size=Pt(11), bold=False,
            color=RGBColor(0x33, 0x33, 0x33),
            align=PP_ALIGN.LEFT, font_name="Calibri"
        )
```

## 範例

### 輸入範例

AI 論壇開場投影片，介紹主講者為某科技公司 CTO：

```python
s = {
    "speaker_name": "Dr. Jane Chen",
    "speaker_title": "CTO, TechCorp Inc.",
    "speaker_photo": "assets/speaker-jane.jpg",
    "expertise_1": "機器學習與 AI 應用",
    "expertise_2": "雲端架構設計",
    "expertise_3": "產品策略與 GTM",
    "expertise_4": "開源社群貢獻",
    "expertise_5": "",
    "linkedin_url": "linkedin.com/in/janec",
    "twitter_url": "@janec_ai",
    "email": "jane@techcorp.com",
    "accent_color": "#2563EB",
    "bg_color": "#F5F5F5",
    "name_font_size": 28,
    "title_font_size": 16,
    "expertise_font_size": 15,
}
```

### 輸出效果

左側顯示圓形頭像佔位（灰色方塊）、藍色大字姓名「Dr. Jane Chen」及灰色職稱。右側頂部有藍色裝飾橫線，下方條列四項核心專長（每項前有藍色小方塊），底部排列 LinkedIn、Twitter、Email 三個社群連結圖示與文字。整體版面乾淨專業，適合正式場合使用。
