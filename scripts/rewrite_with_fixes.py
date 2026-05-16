#!/usr/bin/env python
"""
既存セクションを Opus 4.7 で「修正指示に従って書き直す」スクリプト。
SYSTEM_PROMPT は generate_sections.py を流用(v1.1 ルール込み)。
各セクションの現状ファイルを user メッセージに含めて渡す。
"""
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
sys.path.insert(0, str(ROOT / "scripts"))
import generate_sections as gs  # noqa: E402

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

MODEL = "claude-opus-4-7"
PARALLEL = 8

# 共通仕様(列数設定 + スマホ表示)
COMMON_COLUMNS_MOBILE = """
- セクション settings に「PC の列数」と「スマホ表示方法」を追加(全セクション共通仕様):
  ```json
  { "type": "header", "content": "レイアウト" },
  { "type": "range", "id": "columns_pc", "label": "PC で 1 行に表示する列数", "min": 1, "max": 6, "step": 1, "unit": "列", "default": 3 },
  { "type": "select", "id": "mobile_layout", "label": "スマホでの表示方法",
    "options": [
      { "value": "stack", "label": "1列表示" },
      { "value": "two", "label": "2列表示" },
      { "value": "swipe", "label": "横スワイプ" }
    ],
    "default": "stack" }
  ```
- CSS: PC は `grid-template-columns: repeat({{ section.settings.columns_pc }}, 1fr)` で可変列、
  モバイルは `mobile_layout` に応じて: stack → 1 列 grid / two → 2 列 grid /
  swipe → `display: flex; overflow-x: auto; scroll-snap-type: x mandatory;` で横スワイプ
- 各カード/ブロックには `scroll-snap-align: start` を付けて swipe 時にスナップ
"""


FIXES = {
    "age-group-guide": """
- 共通仕様(列数 + スマホ表示)を追加。
- 既存の「年代ラベル色(セクション設定)」を削除し、各ブロック設定に
  `{ "type": "color", "id": "label_color", "label": "年代ラベルの色", "default": "#7c3aed" }` を追加。
- CSS で年代ラベル色は block.settings.label_color を参照(`style="color: {{ block.settings.label_color }}"`)。
""",
    "allergen-display": """
- 共通仕様(列数 + スマホ表示)を追加。
- アイコン画像を「丸トリミング」で表示:
  CSS で `.alsel-allergen-display__icon { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; aspect-ratio: 1 / 1; }`
""",
    "anchor-link-buttons": """
- セクション名(`{% schema %}` の `name`)を「ページ内アンカーリンク(目次)」に変更(機能がわかりやすい名前)。
- スティッキー動作を確実に動作するよう修正:
  `section.settings.sticky == true` のとき、セクション root に `style="position: sticky; top: 0; z-index: 10;"` を直接付与。
  CSS だけだと親要素の overflow 設定で sticky が効かないことがあるため、インラインで強制。
  さらに親要素の overflow を見越して、`<section>` の直前に空白を入れて確実に sticky にする。
- ブロック設定の `anchor_id` に info を追加:
  "ジャンプ先のセクションの ID 属性(例: features)。リンク先のセクションに <section id='features'> のように同じ ID を設定してください。"
""",
    "assurance-badge": """
- 共通仕様(列数 + スマホ表示)を追加。それ以外の変更は不要。
""",
    "award-certifications": """
- 共通仕様(列数 + スマホ表示)を追加。
- 既存の「受賞年色(セクション設定)」を削除し、各ブロック設定に
  `{ "type": "color", "id": "year_color", "label": "受賞年の色", "default": "#888888" }` を追加。
  CSS で `style="color: {{ block.settings.year_color }}"` を年要素に適用。
- セクション設定にエンブレム画像のトリミング形を追加:
  ```
  { "type": "select", "id": "emblem_shape", "label": "エンブレム画像の形",
    "options": [
      { "value": "circle", "label": "丸くトリミング" },
      { "value": "square", "label": "正方形にトリミング" },
      { "value": "original", "label": "画像そのまま表示" }
    ],
    "default": "circle" }
  ```
  CSS で emblem_shape に応じて画像を切り替え:
  - circle: `border-radius: 50%; aspect-ratio: 1; object-fit: cover;`
  - square: `border-radius: 0; aspect-ratio: 1; object-fit: cover;`
  - original: `border-radius: 0; aspect-ratio: auto; object-fit: contain;`
  実装は `<img class="... alsel-award-certifications__emblem--{{ section.settings.emblem_shape }}">` のような修飾子クラス + CSS で切替。
""",
    "benefits-card": """
- 共通仕様(列数 + スマホ表示)を追加。それ以外の変更は不要。
""",
    "best-seller-ranking": """
- セクション設定に「PC の列数(columns_pc、range 1-6、default 5、unit 列)」のみ追加。
  既存の collection 自動取得・ランキングロジックは変更しない。
- CSS で `grid-template-columns: repeat({{ section.settings.columns_pc }}, 1fr)` を適用。
- モバイル設定(mobile_layout)は不要(このセクションは既に横スクロール風で安定)。
""",
    "blog-cards": """
- スマホ表示方法(mobile_layout、select: stack/two/swipe、default stack)のみ追加。
- 列数(columns_pc)は不要(既存の構造を変えない)。
""",
    "blog-to-product": """
- スマホ表示方法(mobile_layout)のみ追加。列数は不要。
""",
    "brand-stats": """
- スマホ表示方法(mobile_layout)のみ追加。列数は不要(既存の数字を横並びにする設計を維持)。
""",
    "business-calendar": """
- セクション設定に「曜日一括設定」を追加(個別日付指定機能は維持):
  ```json
  { "type": "header", "content": "曜日で一括休業設定" },
  { "type": "checkbox", "id": "holiday_sun", "label": "日曜日を休業日にする", "default": true },
  { "type": "checkbox", "id": "holiday_mon", "label": "月曜日を休業日にする", "default": false },
  { "type": "checkbox", "id": "holiday_tue", "label": "火曜日を休業日にする", "default": false },
  { "type": "checkbox", "id": "holiday_wed", "label": "水曜日を休業日にする", "default": false },
  { "type": "checkbox", "id": "holiday_thu", "label": "木曜日を休業日にする", "default": false },
  { "type": "checkbox", "id": "holiday_fri", "label": "金曜日を休業日にする", "default": false },
  { "type": "checkbox", "id": "holiday_sat", "label": "土曜日を休業日にする", "default": false }
  ```
- ロジック: 各日付セル描画時に「曜日が休業に該当」or「個別日付指定で休業」のどちらかなら休業日扱い。
  既存の `first_dow` / 曜日計算は維持(Zeller の公式そのままで OK)。
""",
    "category-nav": """
- 共通仕様(列数 + スマホ表示)を追加。
- 各ブロックの設定を「カテゴリー画像 + 名前 + リンク手動入力」から「コレクション選択(collection ピッカー)」に変更:
  ```json
  { "type": "collection", "id": "collection", "label": "カテゴリーとして表示するコレクション" },
  { "type": "text", "id": "label_override", "label": "ラベル(空欄なら collection.title を使用)" }
  ```
- 表示は `{%- assign col = collections[block.settings.collection] -%}` で取得し、
  画像は `col.image | image_url` → image_tag、リンクは `col.url`、ラベルは `block.settings.label_override | default: col.title`。
- collection 未設定なら該当ブロックを非表示。
""",
    "collection-features": """
- セクション名(`{% schema %}` の `name`)を「特集カードグリッド」に変更(コレクション選択式ではないことが分かるよう)。
- スマホ表示方法(mobile_layout)を追加。列数(columns_pc)も追加して 1 行表示数を可変に。
""",
}


SYSTEM_PROMPT_REWRITE = (
    gs.SYSTEM_PROMPT
    + "\n\n# 重要(書き直しモード)\n"
    "既存ファイルを下記の指示に従って書き直してください。"
    "**指示にない部分は元のコードをそのまま維持**してください(冒頭 {% comment %} ブロック、\n"
    "{% schema %} の name 以外の既存 settings、preset、CSS スコープ名 alsel-{slug} 等)。\n"
    "出力は完全な Liquid ファイル(前置き禁止、コードフェンス禁止、JSON ラップ禁止)。\n"
    "\n# 共通仕様(列数 + スマホ表示)が指示にある場合の参考実装\n"
    + COMMON_COLUMNS_MOBILE
)


def rewrite_one(slug: str, directive: str):
    p = ROOT / "sections" / f"{slug}.liquid"
    current = p.read_text(encoding="utf-8")
    user_msg = (
        f"# 修正対象\n"
        f"slug: {slug}\n"
        f"ファイルパス: sections/{slug}.liquid\n"
        f"\n"
        f"# 現状のファイル\n"
        f"```liquid\n{current}\n```\n"
        f"\n"
        f"# 修正指示\n"
        f"{directive}\n"
        f"\n"
        f"指示以外の部分は既存コードをそのまま維持。修正後の完全な Liquid コードのみ出力してください。"
    )
    try:
        resp = client.messages.create(
            model=MODEL,
            max_tokens=10000,
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT_REWRITE,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": user_msg}],
        )
        text = "".join(b.text for b in resp.content if hasattr(b, "text"))
        text = re.sub(r"^```(?:liquid|html)?\s*\n", "", text)
        text = re.sub(r"\n```\s*$", "", text).rstrip()
        # 書き出し前にバックアップ
        bak = p.with_suffix(p.suffix + ".pre_p6d.bak")
        if not bak.exists():
            bak.write_text(current, encoding="utf-8")
        p.write_text(text, encoding="utf-8")
        usage = resp.usage
        return {
            "slug": slug,
            "ok": True,
            "lines": text.count("\n") + 1,
            "in": usage.input_tokens,
            "out": usage.output_tokens,
            "cache_read": getattr(usage, "cache_read_input_tokens", 0),
            "cache_create": getattr(usage, "cache_creation_input_tokens", 0),
        }
    except Exception as e:
        return {"slug": slug, "ok": False, "error": str(e)[:200]}


def main():
    items = list(FIXES.items())
    print(
        f"[rewrite] {len(items)} 件、model={MODEL}、parallel={PARALLEL}",
        file=sys.stderr,
    )
    results = []
    t0 = time.time()
    flush_lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=PARALLEL) as pool:
        futures = {pool.submit(rewrite_one, slug, dir_): slug for slug, dir_ in items}
        for fut in as_completed(futures):
            slug = futures[fut]
            r = fut.result()
            with flush_lock:
                results.append(r)
                if r["ok"]:
                    print(
                        f"  OK   {slug} ({r['lines']}行 in {r['in']}/out {r['out']}/cache_read {r['cache_read']})",
                        file=sys.stderr,
                    )
                else:
                    print(f"  ERR  {slug}: {r['error']}", file=sys.stderr)
    elapsed = time.time() - t0

    ok = sum(1 for r in results if r["ok"])
    in_tok = sum(r.get("in", 0) for r in results)
    out_tok = sum(r.get("out", 0) for r in results)
    cache_create = sum(r.get("cache_create", 0) for r in results)
    cache_read = sum(r.get("cache_read", 0) for r in results)
    cost = (
        in_tok * 15 / 1_000_000
        + out_tok * 75 / 1_000_000
        + cache_create * 18.75 / 1_000_000
        + cache_read * 1.5 / 1_000_000
    )
    total = in_tok + cache_create + cache_read
    hit = (cache_read / total) if total else 0
    print(
        f"\n[rewrite] done ok={ok}/{len(items)} elapsed={elapsed:.1f}s\n"
        f"  tokens: in={in_tok} out={out_tok} cache_read={cache_read} cache_create={cache_create}\n"
        f"  hit_rate={hit*100:.1f}% cost=${cost:.4f}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
