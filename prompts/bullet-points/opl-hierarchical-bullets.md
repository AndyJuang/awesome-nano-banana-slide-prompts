---
layout: bullet-points
name: 階層式條列內容頁（二層分組）
tags: [bullet-points, hierarchical, section-header, two-level]
source: 曜捷_公司簡介_簡報草稿_20260310.pptx — Slides 4,6,8,10,12,14
---

# 階層式條列內容頁 Prompt 模版

> 精確尺寸來源：實際 PPTX 解析（13.33" × 7.5"，16:9）

## 版型預覽

```
┌─────────────────────────────────────────────────────────────┐
│  [Logo 右上 9pt]          ■(12.25) ●(11.9) □(12.58)        │
│  ●  標題文字  24pt Bold                                      │
│  ─────────────────────────────────────────────────────────  │
│                                                              │
│  ▌ 分組標題一  15pt Bold                                     │
│    ◆ 條列項目 1-1   14pt                                     │
│    ◆ 條列項目 1-2   14pt                                     │
│    ◆ 條列項目 1-3   14pt                                     │
│                                                              │
│  ▌ 分組標題二  15pt Bold                                     │
│    ◆ 條列項目 2-1   14pt                                     │
│    ◆ 條列項目 2-2   14pt                                     │
│    ◆ 條列項目 2-3   14pt                                     │
│                                                              │
│  ═══════════════════════════════════  底部淺藍細線 #E8F4FD   │
└─────────────────────────────────────────────────────────────┘
```

## 版面精確規格

```
Slide: 13.33" × 7.50"
Background: white (no explicit fill)

── 右上角裝飾 ──
Logo Text:     left=11.30"  top=0.08"  w=1.90"  h=0.45"  9pt Bold brand color
Deco Sq Large: left=12.25"  top=0.22"  w=0.38"  h=0.38"  fill=#1B4F9B
Deco Sq Mid:   left=11.90"  top=0.45"  w=0.24"  h=0.24"  fill=#0091D5
Deco Sq Small: left=12.58"  top=0.52"  w=0.19"  h=0.19"  fill=white border=gray

── 標題列 ──
Title Dot:     left=0.38"  top=0.75"  w=0.22"  h=0.22"  fill=#0091D5
Title Text:    left=0.72"  top=0.62"  w=11.00"  h=0.58"  24pt Bold #404040
Title Line:    left=0.38"  top=1.28"  w=12.00"  h=0.04"  fill=#0091D5

── 內容區（y=1.40" 起）──
分組標題（Section Header）：
  Header Bar:  left=0.38"  top=y  w=0.16"  h=0.30"  fill=#0091D5
  Header Text: left=0.66"  top=y  w=12.00"  h=0.42"  15pt Bold #404040
  (藍色粗竪線 + 文字)

條列項目（Bullet Item）：
  Bullet Dot:  left=0.55"  top=y  w=0.10"  h=0.10"  fill=#0091D5 (小正方形)
  Bullet Text: left=0.78"  top=y  w=12.00"  h=0.40"  14pt normal #404040

間距規律：
  分組標題 y 位置：1.50", 3.70"（兩組），間距 ≈2.20"
  每個條列項目高度 ≈ 0.44"（0.34" text + 0.10" gap）
  分組標題後第一個 bullet：+ 0.57"
  Bullet 間距：+ 0.44"

── 底部裝飾線 ──
Bottom Line:   left=0.38"  top=7.18"  w=12.60"  h=0.05"  fill=#E8F4FD
```

## Core Prompt

```
Generate a hierarchical bullet-point content slide (16:9, 13.33" × 7.50"):

=== TOP RIGHT DECORATIVE ELEMENTS ===
Logo text: "{logo_text}" — 9pt, Bold, {logo_color}
  Position: x=11.30", y=0.08", width=1.90"

Three decorative squares (right side cluster):
  Large:  x=12.25", y=0.22", size=0.38"×0.38", fill={deco_color_1}
  Medium: x=11.90", y=0.45", size=0.24"×0.24", fill={deco_color_2}
  Small:  x=12.58", y=0.52", size=0.19"×0.19", white fill, light gray border

=== TITLE AREA ===
Accent dot:
  Square: x=0.38", y=0.75", size=0.22"×0.22", fill={accent_color}

Title text:
  Text: "{slide_title}" — 24pt, Bold, {title_color}
  Position: x=0.72", y=0.62", width=11.00", height=0.58"

Title underline:
  Rectangle: x=0.38", y=1.28", width=12.00", height=0.04"
  Fill: {accent_color}

=== CONTENT AREA (2-level hierarchy) ===
Starting y ≈ 1.45"

For each group {g} (up to {max_groups} groups):
  Group header:
    Vertical bar: x=0.38", y=y_g, width=0.16", height=0.30", fill={accent_color}
    Header text: "{group_title_g}" — 15pt, Bold, {header_text_color}
      Position: x=0.66", y=y_g, width=12.00", height=0.42"

  For each bullet {b} in group (up to {max_bullets_per_group} items):
    Bullet square: x=0.55", y=y_b, size=0.10"×0.10", fill={bullet_color}
    Bullet text: "{bullet_text_g_b}" — 14pt, normal, {body_text_color}
      Position: x=0.78", y=y_b, width=12.00", height=0.40"

Vertical spacing:
  Group header → first bullet: +0.57"
  Bullet → next bullet: +0.44"
  Last bullet → next group header: +0.50"

=== BOTTOM DECORATION ===
Thin rectangle: x=0.38", y=7.18", width=12.60", height=0.05"
Fill: {bottom_line_color}

Content to fill in:
{content_structure}
  Format:
  Group 1: "{group_1_title}"
    - "{bullet_1_1}"
    - "{bullet_1_2}"
    - "{bullet_1_3}"
  Group 2: "{group_2_title}"
    - "{bullet_2_1}"
    - "{bullet_2_2}"
    - "{bullet_2_3}"
```

## 變數說明

| 變數 | 說明 | 範例值 |
|------|------|--------|
| `{logo_text}` | 右上 Logo 文字 | `{brand_name}` |
| `{logo_color}` | Logo 文字色 | `#1B4F9B` |
| `{deco_color_1}` | 右上大裝飾方塊色 | `#1B4F9B` |
| `{deco_color_2}` | 右上中裝飾方塊色 | `#0091D5` |
| `{accent_color}` | 標題點、底線、分組粗竪線色 | `#0091D5` |
| `{slide_title}` | 投影片主標題 | `{brand_name_cn}：主要業務與競爭優勢` |
| `{title_color}` | 主標題文字色 | `#404040` |
| `{max_groups}` | 最多分組數 | `2`（建議不超過3）|
| `{group_title_g}` | 第 g 組標題 | `核心服務項目` |
| `{header_text_color}` | 分組標題文字色 | `#404040` |
| `{max_bullets_per_group}` | 每組最多條列數 | `4`（建議不超過5）|
| `{bullet_text_g_b}` | 第 g 組第 b 條 | `海運進出口（FCL/LCL）` |
| `{bullet_color}` | 條列小點顏色 | `#0091D5` |
| `{body_text_color}` | 正文色 | `#404040` |
| `{bottom_line_color}` | 底部裝飾線色（極淺） | `#E8F4FD` |
| `{brand_name}` | 品牌名稱（用於 Logo 文字） | `{brand_name}` |
| `{brand_name_cn}` | 品牌中文名稱（用於標題範例） | `{brand_name_cn}` |

## 容量限制與建議

| 情境 | 分組數 | 每組條列 | 總行數 |
|------|--------|---------|-------|
| 最佳 | 2 | 3–4 | 6–8 |
| 最大 | 3 | 3 | 9 |
| 超過時 | 請拆成兩頁 | — | — |

## python-pptx 程式碼骨架

```python
def build_hierarchical_bullets(prs, slide_title, groups,
                                accent_color=None, logo_text="BRAND"):
    """
    建立階層式條列內容頁

    Args:
        slide_title: 投影片標題 (str)
        groups: list of {"title": str, "bullets": [str, ...]}，最多3組
        accent_color: RGBColor，強調色，預設 #0091D5
        logo_text: 右上角 Logo 文字
    """
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

    slide = prs.slides.add_slide(prs.slide_layouts[6])

    if accent_color is None:
        accent_color = RGBColor(0x00, 0x91, 0xD5)

    NAVY = RGBColor(0x1B, 0x4F, 0x9B)
    DARK = RGBColor(64, 64, 64)
    WHITE = RGBColor(255, 255, 255)

    # — 右上角裝飾 —
    add_text_box(slide, logo_text, Inches(11.30), Inches(0.08),
                 Inches(1.90), Inches(0.45), font_size=9, bold=True,
                 color=NAVY, font_name="Calibri")
    add_rect(slide, Inches(12.25), Inches(0.22), Inches(0.38), Inches(0.38),
             fill_color=NAVY)
    add_rect(slide, Inches(11.90), Inches(0.45), Inches(0.24), Inches(0.24),
             fill_color=accent_color)
    add_rect(slide, Inches(12.58), Inches(0.52), Inches(0.19), Inches(0.19),
             fill_color=WHITE, border_color=RGBColor(180, 180, 180))

    # — 標題 —
    add_rect(slide, Inches(0.38), Inches(0.75), Inches(0.22), Inches(0.22),
             fill_color=accent_color)
    add_text_box(slide, slide_title, Inches(0.72), Inches(0.62),
                 Inches(11.00), Inches(0.58), font_size=24, bold=True,
                 color=DARK)
    add_rect(slide, Inches(0.38), Inches(1.28), Inches(12.00), Inches(0.04),
             fill_color=accent_color)

    # — 內容區 —
    y = Inches(1.50)
    GROUP_HEADER_H = Inches(0.42)
    GROUP_BAR_H = Inches(0.30)
    BULLET_H = Inches(0.40)
    HEADER_TO_BULLET = Inches(0.57)
    BULLET_SPACING = Inches(0.44)
    LAST_BULLET_TO_NEXT_GROUP = Inches(0.50)

    for g_idx, group in enumerate(groups[:3]):
        # 分組標題粗竪線
        add_rect(slide, Inches(0.38), y, Inches(0.16), GROUP_BAR_H,
                 fill_color=accent_color)
        # 分組標題文字
        add_text_box(slide, group["title"], Inches(0.66), y,
                     Inches(12.00), GROUP_HEADER_H,
                     font_size=15, bold=True, color=DARK)

        # 條列項目
        by = y + HEADER_TO_BULLET
        for b_idx, bullet in enumerate(group.get("bullets", [])[:5]):
            # 小方點
            add_rect(slide, Inches(0.55), by + Inches(0.15),
                     Inches(0.10), Inches(0.10), fill_color=accent_color)
            # 條列文字
            add_text_box(slide, bullet, Inches(0.78), by,
                         Inches(12.00), BULLET_H,
                         font_size=14, color=DARK)
            by += BULLET_SPACING

        y = by + LAST_BULLET_TO_NEXT_GROUP

    # — 底部裝飾線 —
    add_rect(slide, Inches(0.38), Inches(7.18), Inches(12.60), Inches(0.05),
             fill_color=RGBColor(0xE8, 0xF4, 0xFD))

    return slide
```

## 範例

### 輸入範例
```
標題：{brand_name_cn}：主要業務與競爭優勢
分組1「核心服務項目」：
  - 海運進出口（FCL 整櫃 / LCL 併櫃 / 門到門服務）
  - 空運進出口（時效性高價值貨物全程掌控）
  - 倉儲物流：台北港 ILC / 八里倉 / 台中倉 / 台南南部倉
  - 商務代理及報關、電商代購代運

分組2「數位化與安全優勢」：
  - 全面 EDI 電子資料交換，與船公司及代理即時連線
  - CCTV 出貨全程錄影 ｜ 電腦化倉儲系統即時庫存管理
  - AEO 安全認證（2012 年取得），享有優先快速通關優惠
```

### 輸出效果
白底，右上角三顆深藍/藍色/白色裝飾方塊，
標題「{brand_name_cn}：主要業務與競爭優勢」24pt 粗體 + 藍色底線，
兩個分組各帶藍色粗竪線標題，每組 3–4 個藍色小方點條列，
底部淺藍極細裝飾線
