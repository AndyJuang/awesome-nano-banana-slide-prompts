---
layout: right_img_left_points
tags: [right-img-left-points, image, key-points, split-layout]
updated: 2026-03-16
---

# Right Image + Left Points — 右圖左重點

## 版面規格

```
┌─────────────────────────────────────────────────┐
│ [brand_name]    {slide_title}                   │ ← 頂部細色條 + 標題
│                                                 │
│  • {bullet_1}        ┌──────────────────────┐  │
│  • {bullet_2}        │                      │  │
│  • {bullet_3}        │    {image_path}      │  │ ← 右側圖片（6.30 × 6.20"）
│  • {bullet_4}        │    或深色佔位塊       │  │
│  • {bullet_5}        │                      │  │
│  • {bullet_6}        └──────────────────────┘  │
└─────────────────────────────────────────────────┘
```

**畫布尺寸：** 33.87 × 19.05 cm（16:9 寬螢幕）
**左欄寬度：** ≈ 52%（含邊距）；**右欄寬度：** ≈ 48%
**最大條列數：** 6 條

---

## Core Prompt

Create a **right-image left-points slide** — the mirror layout of left-image right-points. Visual material occupies the right half, while the left side contains a concise bulleted list with accent markers.

**Visual Structure:**
- Background: white
- Top edge: thin `{accent_color}` bar
- Top-left: `{logo_text}` in 9pt brand color
- Slide title: `{slide_title}` at 22pt, bold, left-aligned
- Left half (≈ 6.20" wide): vertical bullet list, each preceded by a small `{accent_color}` rectangle marker
- Right half (≈ 6.30" wide): `{image_path}` image or dark-navy placeholder block

**Bullet Design:**
- Each bullet: thin accent bar on left + 15pt text
- Max 6 bullets; 3–4 is optimal for breathing room
- Avoid sub-bullets — use the separate `opl-hierarchical-bullets` layout instead

---

## 變數說明

| 變數 | 說明 | 範例 |
|------|------|------|
| `{logo_text}` | 左上角品牌標識 | `MY BRAND` |
| `{slide_title}` | 頁面標題 | `核心服務特色` |
| `{accent_color}` | 強調色（色條、標記） | `#0091D5` |
| `{image_path}` | 右側圖片路徑（可省略） | `/images/service.jpg` |
| `{image_caption}` | 圖片說明文字（可省略） | `全球倉儲配送網路` |
| `{bullets}` | 條列陣列（最多 6 條） | `["AEO 安全認證", "24/7 即時追蹤"]` |

---

## python-pptx 骨架

```python
{
  "layout": "right_img_left_points",
  "logo_text": "{logo_text}",
  "slide_title": "{slide_title}",
  "accent_color": "{accent_color}",
  "image_path": "{image_path}",
  "image_caption": "{image_caption}",
  "bullets": [
    "{bullet_1}",
    "{bullet_2}",
    "{bullet_3}",
    "{bullet_4}"
  ]
}
```

---

## 適用情境

- **對外商業提案**：右側展示產品/服務照片，左側列出核心效益
- **專業授課**：右圖為示意圖，左側列出學習要點
- **公司簡介**：右圖為辦公室/工廠，左側列出核心能力
