---
layout: cta
name: 行動呼籲 / 聯絡資訊頁
tags: [cta, qr-code, contact, call-to-action, closing]
---

# 行動呼籲 / 聯絡資訊頁 Prompt 模版

## 版型預覽

```
+--------------------------------------------------+
|  {cta_title}  （大字，品牌色）                    |
|  ─────────────────────────────────────────────── |
|            |                                     |
|  +--------+|  {qr_description}                  |
|  |        ||                                     |
|  |   QR   ||  ✉  {email_address}                |
|  |        ||                                     |
|  +--------+|  🔗  {social_url}                  |
|            |                                     |
|  ─────────────────────────────────────────────── |
|          {brand_tagline}                         |
+--------------------------------------------------+
```
（背景可深色品牌色或白色；左側大型 QR Code 佔位，右側聯絡資訊列）

## 適用情境

- 簡報結尾，引導觀眾掃描 QR Code 取得資料或加入社群
- 活動推廣頁，同時展示多種聯絡方式
- 銷售簡報收尾，提供明確的下一步行動路徑

## Core Prompt

```
Create a 16:9 closing presentation slide with a clear call-to-action and QR code.

BACKGROUND: If {bg_mode} is "dark", fill with {accent_color}. If "light", fill with #FFFFFF. Adapt all text colors accordingly.

TOP SECTION (top 20% of slide):
- "{cta_title}": large bold heading, font size 36pt, color {accent_color} (light mode) or #FFFFFF (dark mode), left-aligned with 6% left margin.
- A horizontal separator line below the title, full width minus margins, 2pt thick, color {accent_color} (light mode) or rgba(255,255,255,0.4) (dark mode).

MIDDLE SECTION (20%–80% of slide), split into two halves:

LEFT HALF (QR Code area, ~40% of slide width):
- A square dark rectangle (#1A1A1A in light mode, #FFFFFF in dark mode) centered in the left half. Size: ~2.8 × 2.8 inches.
- Inside the square, display text "QR" in large font (36pt, bold, contrasting color) centered, to indicate it is a QR code placeholder.
- Below the QR square: small label text "Scan to access" in 11pt, muted color, center-aligned.

RIGHT HALF (contact info, ~60% of slide width):
- "{qr_description}": action instruction text, font size 18pt, bold, same color as heading, top of right half.
- Spacer.
- Email row: A small square icon placeholder in {accent_color} followed by "{email_address}" in 15pt regular text.
- Spacer.
- Social/website row: A small square icon placeholder in {accent_color} followed by "{social_url}" in 15pt regular text.

BOTTOM SECTION (bottom 15% of slide):
- A horizontal separator line.
- "{brand_tagline}": center-aligned, 14pt, muted color (gray in light mode, semi-transparent white in dark mode).
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{cta_title}` | 主行動標題（大字，品牌色） | `Let's Connect` |
| `{qr_description}` | QR Code 旁說明文字 | `掃描領取完整簡報資料` |
| `{email_address}` | 聯絡電子郵件 | `hello@startup.com` |
| `{social_url}` | 社群或網站連結 | `linkedin.com/company/startup` |
| `{brand_tagline}` | 底部品牌標語或 LOGO 文字 | `Startup Inc. · Building the Future` |
| `{accent_color}` | 品牌主色（標題、QR 框、圖示） | `#7C3AED` |
| `{bg_mode}` | 背景模式：`dark` 或 `light` | `light` |

## python-pptx 程式碼骨架

```python
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


def build_cta(slide, s: dict):
    """
    建立行動呼籲 / 聯絡資訊頁版型。
    s 需包含：cta_title, qr_description, email_address, social_url,
              brand_tagline, accent_color, bg_mode ("dark" | "light")
    """
    SLIDE_W = Inches(13.33)
    SLIDE_H = Inches(7.5)

    def hex_to_rgb(h):
        return RGBColor.from_string(h.lstrip("#"))

    bg_mode = s.get("bg_mode", "light")
    accent  = hex_to_rgb(s.get("accent_color", "#7C3AED"))

    if bg_mode == "dark":
        bg_color    = accent
        text_color  = RGBColor(0xFF, 0xFF, 0xFF)
        muted_color = RGBColor(0xCC, 0xCC, 0xCC)
        sep_color   = RGBColor(0xAA, 0xAA, 0xCC)
        qr_fill     = RGBColor(0xFF, 0xFF, 0xFF)
        qr_text_clr = accent
    else:
        bg_color    = RGBColor(0xFF, 0xFF, 0xFF)
        text_color  = RGBColor(0x1A, 0x1A, 0x1A)
        muted_color = RGBColor(0x77, 0x77, 0x77)
        sep_color   = accent
        qr_fill     = RGBColor(0x1A, 0x1A, 0x1A)
        qr_text_clr = RGBColor(0xFF, 0xFF, 0xFF)

    MARGIN = Inches(0.6)

    # ── 背景 ──────────────────────────────────────────────────
    add_rect(slide, Inches(0), Inches(0), SLIDE_W, SLIDE_H,
             fill_color=bg_color)

    # ── 頂部：主行動標題 ──────────────────────────────────────
    title_top = Inches(0.4)
    title_h   = Inches(0.85)
    heading_color = RGBColor(0xFF, 0xFF, 0xFF) if bg_mode == "dark" else accent
    add_text(
        slide, s.get("cta_title", ""),
        left=MARGIN, top=title_top,
        width=SLIDE_W - MARGIN * 2, height=title_h,
        font_size=Pt(36), bold=True,
        color=heading_color,
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )

    # 標題下方分隔線
    sep_top = title_top + title_h + Inches(0.1)
    add_rect(slide, MARGIN, sep_top,
             SLIDE_W - MARGIN * 2, Inches(0.04),
             fill_color=sep_color)

    # ── 中央左側：QR Code 佔位 ────────────────────────────────
    mid_top = sep_top + Inches(0.2)
    qr_size = Inches(2.8)
    left_col_w = SLIDE_W * 0.40
    qr_left = (left_col_w - qr_size) / 2
    qr_top  = mid_top + Inches(0.3)

    add_rect(slide, qr_left, qr_top, qr_size, qr_size,
             fill_color=qr_fill)
    add_text(
        slide, "QR",
        left=qr_left, top=qr_top,
        width=qr_size, height=qr_size,
        font_size=Pt(36), bold=True,
        color=qr_text_clr,
        align=PP_ALIGN.CENTER, font_name="Calibri"
    )

    # QR 底部說明
    add_text(
        slide, "Scan to access",
        left=qr_left, top=qr_top + qr_size + Inches(0.1),
        width=qr_size, height=Inches(0.4),
        font_size=Pt(11), bold=False,
        color=muted_color,
        align=PP_ALIGN.CENTER, font_name="Calibri"
    )

    # ── 中央右側：說明文字與聯絡資訊 ─────────────────────────
    right_left = left_col_w + Inches(0.2)
    right_w    = SLIDE_W - right_left - MARGIN
    icon_size  = Inches(0.28)
    row_h      = Inches(0.55)

    # QR 說明文字
    add_text(
        slide, s.get("qr_description", ""),
        left=right_left, top=mid_top + Inches(0.2),
        width=right_w, height=Inches(0.6),
        font_size=Pt(18), bold=True,
        color=heading_color,
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )

    # Email 列
    email_top = mid_top + Inches(1.2)
    add_rect(slide, right_left, email_top + (row_h - icon_size) / 2,
             icon_size, icon_size, fill_color=accent)
    add_text(
        slide, s.get("email_address", ""),
        left=right_left + icon_size + Inches(0.15), top=email_top,
        width=right_w - icon_size - Inches(0.15), height=row_h,
        font_size=Pt(15), bold=False,
        color=text_color,
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )

    # 社群 / 網站列
    social_top = email_top + row_h + Inches(0.2)
    add_rect(slide, right_left, social_top + (row_h - icon_size) / 2,
             icon_size, icon_size, fill_color=accent)
    add_text(
        slide, s.get("social_url", ""),
        left=right_left + icon_size + Inches(0.15), top=social_top,
        width=right_w - icon_size - Inches(0.15), height=row_h,
        font_size=Pt(15), bold=False,
        color=text_color,
        align=PP_ALIGN.LEFT, font_name="Calibri"
    )

    # ── 底部：分隔線 + 品牌標語 ──────────────────────────────
    bottom_sep_top = SLIDE_H - Inches(1.2)
    add_rect(slide, MARGIN, bottom_sep_top,
             SLIDE_W - MARGIN * 2, Inches(0.04),
             fill_color=sep_color)

    add_text(
        slide, s.get("brand_tagline", ""),
        left=Inches(0), top=bottom_sep_top + Inches(0.15),
        width=SLIDE_W, height=Inches(0.6),
        font_size=Pt(14), bold=False,
        color=muted_color,
        align=PP_ALIGN.CENTER, font_name="Calibri"
    )
```

## 範例

### 輸入範例

新創公司融資簡報結尾，引導投資人掃描 QR Code 取得詳細財務報告：

```python
s = {
    "cta_title": "Let's Connect",
    "qr_description": "掃描領取完整簡報資料",
    "email_address": "hello@startup.com",
    "social_url": "linkedin.com/company/startup",
    "brand_tagline": "Startup Inc. · Building the Future",
    "accent_color": "#7C3AED",
    "bg_mode": "light",
}
```

### 輸出效果

白色背景，頂部紫色大字行動標題「Let's Connect」，下方有紫色分隔線。左側顯示大型黑色 QR Code 佔位方塊（含「QR」文字）及底部小說明文字。右側由上至下排列：說明文字「掃描領取完整簡報資料」、Email 圖示加聯絡地址、LinkedIn 圖示加連結。底部有分隔線及品牌標語，整體清晰易讀，引導觀眾採取行動。
