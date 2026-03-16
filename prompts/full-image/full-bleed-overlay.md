---
layout: full_image
tags: [full-image, overlay, keynote, social-media, atmosphere]
updated: 2026-03-16
---

# Full Image — 全圖疊字頁 (Full-Bleed Overlay)

## 版面規格

```
┌─────────────────────────────────────────────────┐
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ ← 滿版圖片或深色底
│▓ [brand_name]                                 ▓│ ← 左上 Logo（白色半透明）
│▓                                              ▓│
│▓                                              ▓│
│▓              {main_title}                    ▓│ ← 白色大字，垂直置中
│▓              （字少衝擊大）                   ▓│
│▓                                              ▓│
│▓                         {caption}            ▓│ ← 右下或底部說明（可省略）
└─────────────────────────────────────────────────┘
```

**畫布尺寸：** 33.87 × 19.05 cm（16:9 寬螢幕）
**設計原則：** 圖片滿版，文字極少（1-6 個字最佳），深色遮罩提升可讀性

---

## Core Prompt

Create a **full-bleed image slide** with text overlay for maximum atmospheric impact.

**Visual Structure:**
- Background: full-canvas `{image_path}` image (or `{overlay_color}` dark solid placeholder)
- Dark overlay: semi-transparent dark layer to ensure text legibility
- Top-left: `{logo_text}` in small white text (9pt)
- Center: `{main_title}` in `{title_size}`pt (default 54pt), bold, white
- Bottom center (optional): `{caption}` in 18pt, muted white

**Image Guidelines:**
- High-resolution, wide-format photography preferred
- Subject matter: people in action, cityscapes, abstract textures, nature
- Avoid cluttered or text-heavy images
- If no image: use deep navy `#0D1B2A` or brand dark variant

**Typography:**
- 1–6 words maximum for main title
- White (#FFFFFF) or near-white for legibility
- No bullet points; this is a purely visual slide

---

## 變數說明

| 變數 | 說明 | 範例 |
|------|------|------|
| `{logo_text}` | 左上角品牌標識 | `MY BRAND` |
| `{image_path}` | 滿版圖片路徑（可省略，使用佔位色） | `/images/hero.jpg` |
| `{overlay_color}` | 背景/遮罩深色（hex） | `#0D1B2A` |
| `{main_title}` | 疊加主句（1-6 字） | `讓每一票貨，準時抵達` |
| `{caption}` | 底部說明或出處（可省略） | `全球物流合作網路` |
| `{title_size}` | 主標題字號（pt） | `54` |

---

## python-pptx 骨架

```python
{
  "layout": "full_image",
  "logo_text": "{logo_text}",
  "image_path": "{image_path}",
  "overlay_color": "#0D1B2A",
  "main_title": "{main_title}",
  "caption": "{caption}",
  "title_size": 54
}
```

---

## 適用情境

- **大型年度演講 / TED 式演講**：營造情境氛圍，講者道具而非講義
- **社群行銷懶人包**：吸睛首圖，強烈視覺勾引
- **簡報開場或轉場**：章節間的情緒緩衝頁
