#!/usr/bin/env python
"""
ranking-top-three.liquid を Opus 4.7 で完全書き直し。
問題2-6(手動入力廃止 → コレクション自動取得、王冠中央配置、
forloop.index 自動採番、構文修正、フォント継承)を反映。
"""
import os
import re
import sys
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic
import generate_sections as gs

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

EXTRA_REQUIREMENTS = """

# 重要: たけさん指摘の問題対応(必ず反映)
1. 手動入力(product_name / product_image / product_link / product_price)は廃止。
   コレクションピッカー(`{ "type": "collection", "id": "ranking_collection", "label": "ランキング表示するコレクション" }`)を
   1つ用意し、`collections[section.settings.ranking_collection].products | slice: 0, 3` で上位3件を取得する。
2. レイアウト: 表彰台(2位左、1位中央、3位右、モバイルは縦に並ぶ)。
   - 1位の幅を 2位3位より大きく(grid-template-columns で実装)。
   - 商品が3件未満なら、足りない位置は非表示。
3. 順位採番: forloop.index で自動付与。`{%- assign rank = forloop.index -%}` 等。
   - ただし HTML 上の表示順は「2位 → 1位 → 3位」(表彰台順)に並べる必要がある。
     forループ後に必要な並びを生成すること(例: order: 1 → 2 → 3 をループで取得し、
     CSS Grid の `order` プロパティで 1位を中央に配置)。
4. 王冠/メダル: 各カードの上部に「絶対位置で中央配置」する。
   - `position: absolute; top: -18px; left: 50%; transform: translateX(-50%);`
   - 1位は王冠絵文字 👑、2位は 🥈、3位は 🥉 をデフォルト(設定で変更可)。
5. font-family は指定しない(テーマ継承)。font-weight は最大 700 まで。
6. 画像: `{%- assign alt_text = product.title | escape -%}` で先に変数化、
   image_tag の引数は assign 済み変数を渡す(`alt: alt_text`)。
7. 価格: `{{ product.price | money }}` で表示、税込ストアならテーマ設定に従う。
8. 「商品を見る」ボタン: 各カードに `product.url` リンクを付与。

# Liquid 構文の絶対ルール
- image_tag の引数内に `| escape` 等のパイプを書かない。必ず assign で先に変数化。
- フィルタチェーンは1行 or 複数行どちらでも良いが、構文エラーが出ない書き方で。
- `{% if products.size > 0 %}` のような空チェックを必ず入れる(コレクション未選択時の対応)。
- ループ内で `{% if forloop.index > 3 %}{% break %}{% endif %}` で 3件超は無視。
"""


def main():
    target = next(s for s in gs.load_slugs() if s["slug"] == "ranking-top-three")
    user_msg = gs.USER_TEMPLATE.format(
        slug=target["slug"],
        name_ja=target["name_ja"],
        desc_ja=target["desc_ja"],
        category_hint=EXTRA_REQUIREMENTS,
    )

    print(f"[rewrite] {target['slug']} を Opus 4.7 で書き直し...", file=sys.stderr)
    resp = client.messages.create(
        model=gs.MODEL,
        max_tokens=10000,
        system=[
            {
                "type": "text",
                "text": gs.SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(b.text for b in resp.content if hasattr(b, "text"))
    text = re.sub(r"^```(?:liquid|html)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text).rstrip()
    usage = resp.usage
    print(
        f"  in={usage.input_tokens} out={usage.output_tokens} "
        f"cache_create={getattr(usage, 'cache_creation_input_tokens', 0)} "
        f"cache_read={getattr(usage, 'cache_read_input_tokens', 0)}",
        file=sys.stderr,
    )

    out = ROOT / "sections" / "ranking-top-three.liquid"
    # 元のバックアップ
    bak = out.with_suffix(out.suffix + ".pre_rewrite.bak")
    if not bak.exists():
        bak.write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
    out.write_text(text, encoding="utf-8")
    lines = text.count("\n") + 1
    print(f"  -> {out} ({lines} 行)", file=sys.stderr)


if __name__ == "__main__":
    main()
