#!/usr/bin/env python
"""
data/section_slugs.json の各セクションについて、Opus 4.7 で Liquid コードを生成。
出力先: sections/{slug}.liquid

例:
  python scripts/generate_sections.py                  # 全件
  python scripts/generate_sections.py --start 1 --end 5  # 番号 1〜5
  python scripts/generate_sections.py --numbers 1,3,17    # 番号指定
"""
import argparse
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
client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

MODEL = "claude-opus-4-7"
PARALLEL = 8
MAX_RETRIES = 2


SYSTEM_PROMPT = """あなたは Shopify Online Store 2.0 のセクション開発を15年経験している
プロフェッショナルです。日本の EC 事業者向けに「素人でも安心して導入できる
高品質なセクション」を作成します。本作業は ALSEL(日本の EC コンサル企業)
の監修セクションとして liquid-jp.jp 経由で公開されるため、品質基準は最高レベルです。

# 役割
ユーザーから「slug」「セクション名(日本語)」「説明(日本語)」を受け取り、
完全な Shopify セクション(.liquid ファイル本体)を出力します。

# 出力ルール(厳守)
- Liquid コードのみを出力。前置き・解説・コードフェンス・JSON ラップ禁止
- 1ファイル最大 300 行(コメント含む)
- 必ず {% schema %} ブロックを含める
- 必ず presets を 1つ以上定義する(テーマエディタで追加できるように)
- 適切な settings を定義(画像・テキスト・選択肢・カラーなど)
- すべての日本語ラベル・コメントは、ふつうの日本語の常体(である調)

# ファイル冒頭のコメント(必須、{% comment %} 内)
- セクション名(日本語)
- 用途(どんなシーンで使うか、初心者向けの分かりやすい言葉で)
- 推奨設置場所(トップページ・商品ページ・コレクションページなど)
- カスタマイズポイント(テーマエディタで何を変更できるか、箇条書きで)
- 注意点(画像サイズ・依存条件・Online Store 2.0 必須事項など)
- 動作確認バージョン: Online Store 2.0
- ライセンス: ALSEL Original

# CSS スコープ(衝突回避必須)
- セクション内に <style>...</style> を含める
- すべての class は `alsel-{slug}__要素` の BEM 風命名(例: alsel-hero-fv-lp__title)
- グローバル class(.btn / .container など)は使わない
- 必ず `.alsel-{slug}` をルート要素に付与してスコープを担保する
- CSS 変数はセクションスコープのみ(`.alsel-{slug} { --foo: ... }`)

# Liquid 構文ルール
- {% include %} 禁止 → 必要なら {% render 'snippet-name' %} を使う
- 空チェック: `{% if section.settings.heading != blank %}` のように blank チェック
- 画像: `{{ image | image_url: width: 1600 | image_tag: loading: 'lazy', sizes: '...', widths: '...' }}` 形式
- 数値計算: `{{ value | times: 1 }}` のように明示的に数値化してから計算
- セキュリティ: ユーザー入力は必ず `| escape` でエスケープ

# アクセシビリティ
- すべての <img> に alt 属性(空文字でも明示)
- ボタン・リンクの aria-label を適切に
- セクションのルートに aria-label を付ける
- 見出し階層は h2 → h3 の順序を守る(セクション内で h1 は使わない)

# レスポンシブ
- モバイルファースト
- ブレークポイント: 749px(モバイル / PC 境界、Shopify 慣習)
- メディアクエリは最小限、`@media (min-width: 750px)` で PC 拡張

# プリセット(必須、{% schema %} 末尾)
"presets": [
  {
    "name": "ALSEL監修 / {セクション名}",
    "settings": { ... 初心者がそのまま使えるデフォルト値 ... },
    "blocks": [ ... ブロックがあれば初期ブロック ... ]
  }
]

# 設定項目(settings)の命名・説明
- id はスネークケース(例: hero_image / cta_text)
- label は日本語(例: "見出し" / "ボタンの文字" / "背景画像")
- info に初心者向けの説明(例: "推奨サイズ: 1600 × 900px、JPEG または PNG")

---

# 良い例 1: シンプルなヒーローセクション

```liquid
{% comment %}
============================================================
セクション名: シンプルヒーローバナー
用途: トップページのファーストビューで、画像 + 見出し + CTA を一気に伝える
推奨設置場所: トップページの最上部(theme.liquid の index.json 経由)
カスタマイズポイント:
  - 背景画像(推奨 1600 × 900px)
  - 見出し・サブコピー
  - CTA ボタン(リンク先、文字)
  - 文字色・配置
注意点:
  - 画像は WebP も自動生成される(Shopify CDN)
  - 1セクションで完結。複数並べたい場合は presets から追加
動作確認バージョン: Online Store 2.0
ライセンス: ALSEL Original
============================================================
{% endcomment %}

<section class="alsel-hero-simple" aria-label="{{ section.settings.heading | escape }}">
  {%- if section.settings.background_image != blank -%}
    {{ section.settings.background_image
      | image_url: width: 1600
      | image_tag: loading: 'lazy', class: 'alsel-hero-simple__bg', alt: section.settings.heading | escape, widths: '375, 750, 1100, 1500, 1600' }}
  {%- endif -%}
  <div class="alsel-hero-simple__inner">
    {%- if section.settings.heading != blank -%}
      <h2 class="alsel-hero-simple__title">{{ section.settings.heading }}</h2>
    {%- endif -%}
    {%- if section.settings.subheading != blank -%}
      <p class="alsel-hero-simple__sub">{{ section.settings.subheading }}</p>
    {%- endif -%}
    {%- if section.settings.cta_text != blank and section.settings.cta_link != blank -%}
      <a class="alsel-hero-simple__cta" href="{{ section.settings.cta_link }}">
        {{ section.settings.cta_text }}
      </a>
    {%- endif -%}
  </div>
</section>

<style>
  .alsel-hero-simple { position: relative; overflow: hidden; min-height: 60vh; }
  .alsel-hero-simple__bg { width: 100%; height: 100%; object-fit: cover; position: absolute; inset: 0; z-index: 0; }
  .alsel-hero-simple__inner { position: relative; z-index: 1; padding: 4rem 1.5rem; max-width: 720px; margin: 0 auto; color: {{ section.settings.text_color }}; text-align: {{ section.settings.text_align }}; }
  .alsel-hero-simple__title { font-size: clamp(1.6rem, 5vw, 3rem); font-weight: 800; line-height: 1.3; margin: 0 0 1rem; }
  .alsel-hero-simple__sub { font-size: 1rem; line-height: 1.6; margin: 0 0 1.5rem; }
  .alsel-hero-simple__cta { display: inline-block; padding: 0.9rem 2rem; background: {{ section.settings.cta_bg }}; color: {{ section.settings.cta_color }}; text-decoration: none; border-radius: 9999px; font-weight: 700; }
  @media (min-width: 750px) {
    .alsel-hero-simple__inner { padding: 6rem 2rem; }
  }
</style>

{% schema %}
{
  "name": "ヒーロー(シンプル)",
  "tag": "section",
  "class": "alsel-section",
  "settings": [
    { "type": "image_picker", "id": "background_image", "label": "背景画像", "info": "推奨 1600 × 900px、JPEG または PNG" },
    { "type": "text", "id": "heading", "label": "見出し", "default": "メインキャッチ" },
    { "type": "text", "id": "subheading", "label": "サブコピー", "default": "サブの説明文がここに入る。" },
    { "type": "text", "id": "cta_text", "label": "ボタンの文字", "default": "詳しく見る" },
    { "type": "url", "id": "cta_link", "label": "ボタンのリンク先" },
    { "type": "color", "id": "text_color", "label": "文字色", "default": "#ffffff" },
    { "type": "color", "id": "cta_bg", "label": "ボタン背景色", "default": "#6d28d9" },
    { "type": "color", "id": "cta_color", "label": "ボタン文字色", "default": "#ffffff" },
    { "type": "select", "id": "text_align", "label": "文字の配置",
      "options": [
        { "value": "left", "label": "左寄せ" },
        { "value": "center", "label": "中央" },
        { "value": "right", "label": "右寄せ" }
      ],
      "default": "center" }
  ],
  "presets": [
    {
      "name": "ALSEL監修 / ヒーロー(シンプル)",
      "settings": {
        "heading": "メインキャッチ",
        "subheading": "サブコピーで補足説明を入れる。"
      }
    }
  ]
}
{% endschema %}
```

# 良い例 2: ブロック型(3つの選ばれる理由)

```liquid
{% comment %}
============================================================
セクション名: 3つの選ばれる理由
用途: ストアの信頼性を訴求する定番セクション
推奨設置場所: トップページ・商品ページ・LP の途中(ヒーロー直後など)
カスタマイズポイント:
  - 各理由のアイコン画像・タイトル・本文
  - 背景色
  - ブロックの追加・削除でカード数を変更
注意点:
  - アイコンは正方形(推奨 200 × 200px、PNG 透過)を 3 枚用意する
  - ブロックは 3〜6 個推奨。それ以外は CSS で grid 数を調整する必要あり
動作確認バージョン: Online Store 2.0
ライセンス: ALSEL Original
============================================================
{% endcomment %}

<section class="alsel-reasons-three" aria-label="選ばれる理由">
  {%- if section.settings.heading != blank -%}
    <h2 class="alsel-reasons-three__heading">{{ section.settings.heading }}</h2>
  {%- endif -%}
  <div class="alsel-reasons-three__grid">
    {%- for block in section.blocks -%}
      <article class="alsel-reasons-three__card" {{ block.shopify_attributes }}>
        {%- if block.settings.icon != blank -%}
          {{ block.settings.icon | image_url: width: 200 | image_tag: loading: 'lazy', class: 'alsel-reasons-three__icon', alt: block.settings.title | escape }}
        {%- endif -%}
        <h3 class="alsel-reasons-three__title">{{ block.settings.title }}</h3>
        <p class="alsel-reasons-three__body">{{ block.settings.body }}</p>
      </article>
    {%- endfor -%}
  </div>
</section>

<style>
  .alsel-reasons-three { padding: 3rem 1rem; background: {{ section.settings.bg_color }}; }
  .alsel-reasons-three__heading { font-size: clamp(1.4rem, 4vw, 2.2rem); text-align: center; margin: 0 0 2rem; }
  .alsel-reasons-three__grid { display: grid; grid-template-columns: 1fr; gap: 1.5rem; max-width: 1100px; margin: 0 auto; }
  .alsel-reasons-three__card { text-align: center; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
  .alsel-reasons-three__icon { width: 80px; height: 80px; object-fit: contain; margin: 0 auto 1rem; }
  .alsel-reasons-three__title { font-size: 1.15rem; font-weight: 700; margin: 0 0 0.75rem; }
  .alsel-reasons-three__body { font-size: 0.95rem; line-height: 1.7; color: #475569; margin: 0; }
  @media (min-width: 750px) {
    .alsel-reasons-three { padding: 5rem 2rem; }
    .alsel-reasons-three__grid { grid-template-columns: repeat(3, 1fr); }
  }
</style>

{% schema %}
{
  "name": "3つの選ばれる理由",
  "tag": "section",
  "class": "alsel-section",
  "settings": [
    { "type": "text", "id": "heading", "label": "セクション見出し", "default": "選ばれる理由" },
    { "type": "color", "id": "bg_color", "label": "背景色", "default": "#f8fafc" }
  ],
  "blocks": [
    {
      "type": "reason",
      "name": "理由カード",
      "settings": [
        { "type": "image_picker", "id": "icon", "label": "アイコン画像", "info": "推奨 200 × 200px、PNG 透過" },
        { "type": "text", "id": "title", "label": "タイトル", "default": "ポイント名" },
        { "type": "textarea", "id": "body", "label": "本文", "default": "理由の説明文がここに入る。" }
      ]
    }
  ],
  "presets": [
    {
      "name": "ALSEL監修 / 3つの選ばれる理由",
      "blocks": [
        { "type": "reason", "settings": { "title": "高品質", "body": "厳選した素材を使っている。" } },
        { "type": "reason", "settings": { "title": "送料無料", "body": "5000 円以上のご注文で送料無料。" } },
        { "type": "reason", "settings": { "title": "安心保証", "body": "30 日間の返品保証付き。" } }
      ]
    }
  ]
}
{% endschema %}
```

# 出力前の最終チェック(自己レビュー)
1. 冒頭 {% comment %} ブロックがある(全項目記載)
2. <section class="alsel-{slug}" aria-label="..."> でラップされている
3. <style> でスコープ付き CSS がある(全 class が alsel-{slug}__ プレフィックス)
4. {% schema %} の name / settings / presets が完備
5. presets[0].name が "ALSEL監修 / {セクション名}" 形式
6. {% include %} を使っていない
7. すべての settings の label が日本語
8. 300 行以内

これらをすべて満たした完璧な Liquid コードのみを出力してください。
"""


USER_TEMPLATE = """# 生成依頼

slug: {slug}
セクション名(日本語): {name_ja}
説明: {desc_ja}

上記のセクションを、SYSTEM プロンプトのルールに従って完全実装してください。
出力は Liquid コードのみ(前置き禁止、コードフェンス禁止、JSON ラップ禁止)。
"""


def load_slugs():
    return json.loads((ROOT / "data" / "section_slugs.json").read_text(encoding="utf-8"))


def generate_one(rec):
    slug = rec["slug"]
    user_msg = USER_TEMPLATE.format(
        slug=slug, name_ja=rec["name_ja"], desc_ja=rec["desc_ja"]
    )
    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=8000,
                system=[
                    {
                        "type": "text",
                        "text": SYSTEM_PROMPT,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[{"role": "user", "content": user_msg}],
            )
            text = "".join(b.text for b in resp.content if hasattr(b, "text"))
            # フェンス除去
            text = re.sub(r"^```(?:liquid|html)?\s*\n", "", text)
            text = re.sub(r"\n```\s*$", "", text).rstrip()
            usage = {
                "in": resp.usage.input_tokens,
                "out": resp.usage.output_tokens,
                "cache_create": getattr(resp.usage, "cache_creation_input_tokens", 0),
                "cache_read": getattr(resp.usage, "cache_read_input_tokens", 0),
            }
            return {**rec, "code": text, "usage": usage, "error": None}
        except Exception as e:
            if attempt >= MAX_RETRIES:
                return {**rec, "code": "", "usage": None, "error": str(e)}
            time.sleep(2 * (attempt + 1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--numbers", help="番号 csv (例: 1,2,3)")
    parser.add_argument("--start", type=int, default=None)
    parser.add_argument("--end", type=int, default=None)
    parser.add_argument("--out-dir", default="sections")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    slugs = load_slugs()
    if args.numbers:
        target_nums = set(int(x) for x in args.numbers.split(","))
        targets = [s for s in slugs if s["number"] in target_nums]
    elif args.start is not None and args.end is not None:
        targets = [s for s in slugs if args.start <= s["number"] <= args.end]
    else:
        targets = slugs

    out_dir = ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    if not args.overwrite:
        before = len(targets)
        targets = [s for s in targets if not (out_dir / f"{s['slug']}.liquid").exists()]
        skipped = before - len(targets)
        if skipped:
            print(f"[gen] skipped existing: {skipped}", file=sys.stderr)

    print(f"[gen] target={len(targets)} model={MODEL} parallel={PARALLEL}", file=sys.stderr)
    if not targets:
        print("[gen] nothing to do", file=sys.stderr)
        return

    results = []
    flush_lock = threading.Lock()
    t0 = time.time()
    completed = 0
    with ThreadPoolExecutor(max_workers=PARALLEL) as pool:
        futures = {pool.submit(generate_one, rec): rec for rec in targets}
        for fut in as_completed(futures):
            rec = futures[fut]
            res = fut.result()
            results.append(res)
            if res["error"]:
                print(
                    f"  ERR  [{rec['number']:>3}] {rec['slug']}: {res['error'][:100]}",
                    file=sys.stderr,
                )
                continue
            out_path = out_dir / f"{rec['slug']}.liquid"
            with flush_lock:
                out_path.write_text(res["code"], encoding="utf-8")
            lines = res["code"].count("\n") + 1
            completed += 1
            print(
                f"  OK   [{rec['number']:>3}] {rec['slug']} ({lines}行 "
                f"in {res['usage']['in']}/out {res['usage']['out']}/cache_read {res['usage']['cache_read']})",
                file=sys.stderr,
            )
    elapsed = time.time() - t0

    ok = [r for r in results if r["error"] is None]
    ng = [r for r in results if r["error"]]
    in_tok = sum((r["usage"] or {}).get("in", 0) for r in results)
    out_tok = sum((r["usage"] or {}).get("out", 0) for r in results)
    cache_create = sum((r["usage"] or {}).get("cache_create", 0) for r in results)
    cache_read = sum((r["usage"] or {}).get("cache_read", 0) for r in results)
    total_input = in_tok + cache_create + cache_read
    hit_rate = (cache_read / total_input) if total_input else 0.0
    # Opus 4.7 価格: $15/M input, $75/M output, cache write +25%, cache read 10%
    cost = (
        in_tok * 15.0 / 1_000_000
        + out_tok * 75.0 / 1_000_000
        + cache_create * 18.75 / 1_000_000
        + cache_read * 1.5 / 1_000_000
    )
    print(
        f"\n[gen] done: ok={len(ok)} err={len(ng)} elapsed={elapsed:.1f}s\n"
        f"  tokens: input={in_tok} output={out_tok}\n"
        f"  cache: create={cache_create} read={cache_read} hit_rate={hit_rate*100:.1f}%\n"
        f"  est_cost: ${cost:.4f}",
        file=sys.stderr,
    )

    meta = {
        "model": MODEL,
        "elapsed_seconds": round(elapsed, 1),
        "ok": len(ok),
        "err": len(ng),
        "input_tokens": in_tok,
        "output_tokens": out_tok,
        "cache_creation_input_tokens": cache_create,
        "cache_read_input_tokens": cache_read,
        "cache_hit_rate": round(hit_rate, 4),
        "est_cost_usd": round(cost, 6),
    }
    meta_path = ROOT / "data" / "section_gen_meta.json"
    meta_path.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[gen] meta -> {meta_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
