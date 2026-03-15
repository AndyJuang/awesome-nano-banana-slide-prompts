# 🍌 Awesome Nano Banana Slide Prompts

A curated collection of presentation slide layout prompt templates — deconstruct any slide into reusable, parameterized prompts.

## Layout Categories

| Layout | Folder | Description |
|--------|--------|-------------|
| 封面頁 Cover | [`prompts/cover/`](prompts/cover/) | Opening slide with brand identity |
| 大標題頁 Big Title | [`prompts/big-title/`](prompts/big-title/) | Dominant heading with minimal supporting text |
| 章節分隔頁 Section Divider | [`prompts/section-divider/`](prompts/section-divider/) | Transition slide between major sections |
| 條列式重點 Bullet Points | [`prompts/bullet-points/`](prompts/bullet-points/) | Structured list of key points |
| 表格頁 Table | [`prompts/table/`](prompts/table/) | Data or comparison table |
| 左圖右重點 Left Image + Right Points | [`prompts/left-img-right-points/`](prompts/left-img-right-points/) | Visual-left, text-right split layout |
| 右圖左重點 Right Image + Left Points | [`prompts/right-img-left-points/`](prompts/right-img-left-points/) | Text-left, visual-right split layout |
| 雙欄對比 Two Columns | [`prompts/two-columns/`](prompts/two-columns/) | Side-by-side comparison or contrast |
| 全圖頁 Full Image | [`prompts/full-image/`](prompts/full-image/) | Full-bleed image with text overlay |
| 數據圖表 Data / Chart | [`prompts/data-chart/`](prompts/data-chart/) | Charts, KPIs, and data visualizations |

## How to Use

1. Find the layout closest to what you need
2. Copy the prompt from the layout's `.md` file
3. Replace `{variables}` with your content
4. Feed the prompt to your AI slide generator (Claude, GPT, Gemini, etc.)

## How Prompts Are Generated

Each prompt template is created using the `/nano-banana-slide` Claude Code skill:

1. Provide a slide screenshot or description
2. The skill deconstructs the layout into a parameterized prompt
3. The output is saved to the appropriate category folder

## Contributing

Add a new prompt by running:
```
/nano-banana-slide
```
Then follow the prompts to describe or upload your slide example.

## Prompt File Format

Each prompt file follows this structure:

```markdown
---
layout: {layout-id}
name: {Layout Name}
tags: [tag1, tag2]
---

# Layout Name Prompt Template

## Layout Preview
[ASCII diagram]

## Core Prompt
[The actual prompt with {variables}]

## Variable Reference
[Table of all variables]
```

---

*Generated with [Claude Code](https://claude.ai/claude-code) · `/nano-banana-slide` skill*
