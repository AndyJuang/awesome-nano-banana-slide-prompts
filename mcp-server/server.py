"""
nano-banana-slides MCP Server
提供三個工具：
  - list_layouts         列出所有可用版型
  - get_layout_prompt    取得版型的 Prompt 模版內容
  - build_presentation   根據投影片計劃生成 PPTX 草稿
"""
import sys
import json
import asyncio
from pathlib import Path

# 將 mcp-server 目錄加入 import 路徑
sys.path.insert(0, str(Path(__file__).parent))

from fastmcp import FastMCP

REPO_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"

mcp = FastMCP(
    name="nano-banana-slides",
    instructions="""
簡報版型 Prompt 庫 + PPTX 生成 MCP 伺服器。

可用工具：
1. list_layouts         — 列出所有版型分類與檔案名稱
2. get_layout_prompt    — 取得特定版型的完整 Prompt 模版
3. build_presentation   — 傳入投影片計劃 JSON，直接生成 .pptx 草稿

典型使用流程：
  用戶提供簡報需求 → 呼叫 list_layouts 確認可用版型
  → 規劃 slide_plan JSON → 呼叫 build_presentation 生成 PPTX
""",
)


@mcp.tool
async def list_layouts() -> str:
    """
    列出所有可用的投影片版型分類與對應的 Prompt 模版檔案。

    回傳 JSON，格式：
    {
      "cover": ["basic-cover", "opl-photo-split-cover", ...],
      "bullet-points": [...],
      ...
    }

    build_presentation 支援的 layout 值：
      cover | closing | contents | section_divider | bullet_points | table
    """
    result = {}
    for cat in sorted(PROMPTS_DIR.iterdir()):
        if cat.is_dir() and not cat.name.startswith("."):
            files = sorted(f.stem for f in cat.glob("*.md") if not f.name.startswith("_"))
            if files:
                result[cat.name] = files
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool
async def get_layout_prompt(category: str, filename: str) -> str:
    """
    取得特定版型的完整 Prompt 模版（含版面規格、Core Prompt、變數說明、程式碼骨架）。

    Args:
        category: 版型分類，例如 "cover"、"bullet-points"、"section-divider"、"contents"
        filename: 檔名（不含 .md），例如 "opl-photo-split-cover"、"opl-hierarchical-bullets"

    用 list_layouts 查看所有可用的 category / filename 組合。
    """
    path = PROMPTS_DIR / category / f"{filename}.md"
    if not path.exists():
        available = [
            str(p.relative_to(PROMPTS_DIR))
            for p in PROMPTS_DIR.rglob("*.md")
            if not p.name.startswith("_")
        ]
        return (
            f"找不到版型：{category}/{filename}.md\n\n"
            f"可用版型：\n" + "\n".join(f"  {a}" for a in sorted(available))
        )
    return path.read_text(encoding="utf-8")


@mcp.tool
async def build_presentation(
    output_filename: str,
    slide_plan: str,
    output_dir: str = ".",
) -> str:
    """
    根據投影片計劃生成 PPTX 草稿檔案。

    Args:
        output_filename: 輸出檔名，例如 "公司簡介.pptx"
        output_dir:      輸出目錄（絕對路徑或相對路徑，預設當前目錄）
        slide_plan:      JSON 字串，投影片清單（見下方格式說明）

    ─── slide_plan 格式 ───────────────────────────────────────────────────────

    每張投影片為一個 JSON 物件，必須含 "layout" 欄位。

    支援的 layout 及對應欄位：

    ① cover（封面頁）
    {
      "layout": "cover",
      "brand_name_line_1": "MY BRAND",       // 右側色塊第一行大字
      "brand_name_line_2": "GROUP",           // 右側色塊第二行大字
      "main_title": "公司簡介 2026",           // 下半主標題
      "subtitle": "MY BRAND CO., LTD.",       // 副標題
      "logo_text": "MY BRAND",               // 左上角 Logo 文字
      "brand_color": "#1B4F9B",              // 品牌色（hex）
      "cta_text": "START",                   // 按鈕文字（可省略）
      "partner_text": "Partner of XYZ",      // 右下備注（可省略）
      "image_paths": [null, null, null]      // 三張照片路徑，null 用深色佔位塊
    }

    ② closing（結尾頁，與封面相同佈局）
    {
      "layout": "closing",
      "closing_primary": "感謝您",
      "closing_secondary": "Thank you",
      "logo_text": "MY BRAND",
      "brand_color": "#1B4F9B"
    }

    ③ contents（目錄頁）
    {
      "layout": "contents",
      "label_primary": "目錄",
      "label_secondary": "contents",
      "logo_text": "MY BRAND",
      "panel_color": "#2D415F",              // 左欄背景色（可省略）
      "items": [                             // 最多 6 項
        {"title": "公司背景", "subtitle": "BACKGROUND"},
        {"title": "主要業務", "subtitle": "SERVICES"},
        {"title": "合作夥伴", "subtitle": "PARTNERS"}
      ]
    }

    ④ section_divider（章節分隔頁）
    {
      "layout": "section_divider",
      "part_number": 1,                      // 章節編號（1–10）
      "section_title": "公司背景",
      "logo_text": "MY BRAND",
      "brand_color": "#1B4F9B",
      "accent_color": "#0091D5"              // 可省略
    }

    ⑤ bullet_points（條列式內容頁）
    {
      "layout": "bullet_points",
      "slide_title": "公司背景 — 基本資料",
      "logo_text": "MY BRAND",
      "accent_color": "#0091D5",             // 可省略
      "groups": [                            // 最多 3 組，每組最多 5 條
        {
          "title": "基本資料",
          "bullets": ["成立時間：2001 年", "員工：300 人", "總部：台北"]
        },
        {
          "title": "核心特色",
          "bullets": ["全球合作 60+ 國", "AEO 安全認證", "24/7 即時追蹤"]
        }
      ]
    }

    ⑥ table（表格頁）
    {
      "layout": "table",
      "slide_title": "服務方案比較",
      "logo_text": "MY BRAND",
      "accent_color": "#0091D5",
      "col_headers": ["項目", "基本版", "專業版", "企業版"],
      "rows_data": [
        ["倉儲空間", "500m²", "2,000m²", "無限制"],
        ["配送次數", "5次/月", "20次/月", "無限制"],
        ["客服支援", "email", "電話", "專屬顧問"]
      ]
    }

    ─── 完整範例 ───────────────────────────────────────────────────────────────

    slide_plan = '[
      {"layout":"cover","brand_name_line_1":"MY BRAND","brand_name_line_2":"GROUP",
       "main_title":"公司簡介 2026","subtitle":"MY BRAND CO., LTD.",
       "logo_text":"MY BRAND","brand_color":"#1B4F9B"},
      {"layout":"contents","label_primary":"目錄","label_secondary":"contents",
       "logo_text":"MY BRAND",
       "items":[{"title":"公司背景","subtitle":"BACKGROUND"},
                {"title":"主要業務","subtitle":"SERVICES"}]},
      {"layout":"section_divider","part_number":1,"section_title":"公司背景",
       "logo_text":"MY BRAND"},
      {"layout":"bullet_points","slide_title":"公司背景 — 基本資料",
       "logo_text":"MY BRAND",
       "groups":[{"title":"基本資料","bullets":["成立：2001年","員工：300人"]},
                 {"title":"核心特色","bullets":["全球網路","AEO認證"]}]},
      {"layout":"closing","closing_primary":"感謝您",
       "closing_secondary":"Thank you","logo_text":"MY BRAND"}
    ]'
    """
    from slide_builders import build_presentation_from_plan

    try:
        plan = json.loads(slide_plan)
    except json.JSONDecodeError as e:
        return f"❌ slide_plan JSON 格式錯誤：{e}\n請確認引號、括號完整。"

    if not isinstance(plan, list) or len(plan) == 0:
        return "❌ slide_plan 必須是非空的 JSON 陣列。"

    out_path = Path(output_dir).expanduser() / output_filename
    try:
        result = build_presentation_from_plan(plan, out_path)
        return (
            f"✅ 簡報已生成：{result}\n"
            f"共 {len(plan)} 張投影片\n"
            f"使用版型：{', '.join(s.get('layout','?') for s in plan)}"
        )
    except Exception as e:
        import traceback
        return f"❌ 生成失敗：{e}\n{traceback.format_exc()}"


if __name__ == "__main__":
    asyncio.run(mcp.run_stdio())
