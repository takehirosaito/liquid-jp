#!/usr/bin/env python
"""
日本語化結果を Markdown レポートに変換。--compare-with で v1 比較フッター付きにできる。
"""
import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = datetime.now().strftime("%Y%m%d")


def code_block(code, lang="liquid", max_lines=40):
    lines = code.splitlines()
    omitted = 0
    if len(lines) > max_lines:
        omitted = len(lines) - max_lines
        lines = lines[:max_lines]
    body = "\n".join(lines)
    suffix = f"\n... (以下 {omitted} 行省略)" if omitted else ""
    return f"```{lang}\n{body}{suffix}\n```"


def fmt_record(idx, rec):
    t = rec.get("translation") or {}
    if rec.get("error"):
        return (
            f"### {idx}. ❌ ERROR — {rec['file_name']}\n\n"
            f"- 出典: [{rec['repo_owner']}/{rec['repo_name']}]({rec['raw_url']})\n"
            f"- エラー: `{rec['error']}`\n"
        )
    is_ref = rec["source_kind"].startswith("reference")
    badge = "📘 リファレンス" if is_ref else "🧩 スニペット"
    lang = "json" if is_ref else "liquid"
    tags = t.get("tags") or []
    tags_str = " ".join(f"`{x}`" for x in tags) if tags else "—"
    return (
        f"### {idx}. {badge} {t.get('title_ja') or '(タイトル未生成)'}\n\n"
        f"**カテゴリ:** {t.get('category', '—')} ／ **難易度:** {t.get('difficulty', '—')} "
        f"／ **タグ:** {tags_str}\n\n"
        f"- **出典:** [`{rec['repo_owner']}/{rec['repo_name']}`]({rec['raw_url']}) "
        f"（ライセンス: {rec['license']}、{rec['line_count']}行）\n"
        f"- **ファイル:** `{rec['file_path']}`\n\n"
        f"**説明:** {t.get('description_ja', '—')}\n\n"
        f"**用途:** {t.get('use_case_ja', '—')}\n\n"
        f"**設置場所:** {t.get('where_to_paste_ja', '—')}\n\n"
        f"**注意点:** {t.get('caveats_ja', '—')}\n\n"
        f"<details><summary>コード({rec['line_count']}行)を見る</summary>\n\n"
        f"{code_block(rec['code'], lang=lang)}\n\n"
        f"</details>\n"
    )


def aggregate(records):
    cat_counter = Counter()
    diff_counter = Counter()
    by_repo = defaultdict(int)
    in_tok = out_tok = cache_create = cache_read = 0
    for r in records:
        t = r.get("translation") or {}
        if t:
            cat_counter[t.get("category", "—")] += 1
            diff_counter[t.get("difficulty", "—")] += 1
        by_repo[r["repo_name"]] += 1
        u = r.get("usage") or {}
        in_tok += u.get("input_tokens", 0)
        out_tok += u.get("output_tokens", 0)
        cache_create += u.get("cache_creation_input_tokens", 0)
        cache_read += u.get("cache_read_input_tokens", 0)
    cost = (
        in_tok * 1.0 / 1_000_000
        + out_tok * 5.0 / 1_000_000
        + cache_create * 1.25 / 1_000_000
        + cache_read * 0.1 / 1_000_000
    )
    return {
        "categories": cat_counter,
        "difficulty": diff_counter,
        "by_repo": by_repo,
        "input_tokens": in_tok,
        "output_tokens": out_tok,
        "cache_creation": cache_create,
        "cache_read": cache_read,
        "cost": cost,
    }


def load_meta(jsonl_path):
    meta_path = jsonl_path.with_suffix(".meta.json")
    if meta_path.exists():
        try:
            return json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception:
            return None
    return None


def build_comparison_section(v2_records, v2_meta, v1_jsonl):
    v1_records = [json.loads(l) for l in v1_jsonl.open(encoding="utf-8")]
    v1_agg = aggregate(v1_records)
    v2_agg = aggregate(v2_records)
    v1_meta = load_meta(v1_jsonl)

    lines = ["## 比較: v1 vs v2", ""]
    lines.append("### 実行コスト・処理")
    lines.append("")
    lines.append("| 項目 | v1 (旧プロンプト) | v2 (新プロンプト) | 差分 |")
    lines.append("|---|---:|---:|---:|")

    def row(label, v1v, v2v, fmt="{:,}"):
        try:
            diff = v2v - v1v
            sign = "+" if diff > 0 else ""
            return f"| {label} | {fmt.format(v1v)} | {fmt.format(v2v)} | {sign}{fmt.format(diff)} |"
        except Exception:
            return f"| {label} | {v1v} | {v2v} | — |"

    v1_elapsed = (v1_meta or {}).get("elapsed_seconds")
    v2_elapsed = (v2_meta or {}).get("elapsed_seconds")
    lines.append(
        f"| 処理時間（秒） | "
        f"{v1_elapsed if v1_elapsed is not None else '—'} | "
        f"{v2_elapsed if v2_elapsed is not None else '—'} | — |"
    )
    lines.append(row("入力 tokens", v1_agg["input_tokens"], v2_agg["input_tokens"]))
    lines.append(row("出力 tokens", v1_agg["output_tokens"], v2_agg["output_tokens"]))
    lines.append(row("キャッシュ作成 tokens", v1_agg["cache_creation"], v2_agg["cache_creation"]))
    lines.append(row("キャッシュ読込 tokens", v1_agg["cache_read"], v2_agg["cache_read"]))
    lines.append(
        f"| 推定コスト (USD) | ${v1_agg['cost']:.4f} | ${v2_agg['cost']:.4f} | "
        f"{'+' if v2_agg['cost'] > v1_agg['cost'] else ''}${v2_agg['cost'] - v1_agg['cost']:.4f} |"
    )
    lines.append("")

    lines.append("### カテゴリ分布の変化")
    lines.append("")
    cats = set(v1_agg["categories"]) | set(v2_agg["categories"])
    rows_sorted = sorted(
        cats,
        key=lambda c: -(v2_agg["categories"].get(c, 0) + v1_agg["categories"].get(c, 0)),
    )
    lines.append("| カテゴリ | v1 | v2 | 差分 |")
    lines.append("|---|---:|---:|---:|")
    for c in rows_sorted:
        v1c = v1_agg["categories"].get(c, 0)
        v2c = v2_agg["categories"].get(c, 0)
        diff = v2c - v1c
        sign = "+" if diff > 0 else ""
        lines.append(f"| {c} | {v1c} | {v2c} | {sign}{diff} |")
    lines.append("")

    lines.append("### 難易度分布の変化")
    lines.append("")
    lines.append("| 難易度 | v1 | v2 |")
    lines.append("|---|---:|---:|")
    for d in ["初級", "中級", "上級"]:
        lines.append(f"| {d} | {v1_agg['difficulty'].get(d, 0)} | {v2_agg['difficulty'].get(d, 0)} |")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="data/translated_50.jsonl")
    parser.add_argument(
        "--dst", default=None, help="output md path (default: output/sample_report_YYYYMMDD.md)"
    )
    parser.add_argument(
        "--compare-with",
        default=None,
        help="path to a v1 translated jsonl for comparison footer",
    )
    parser.add_argument("--title", default="liquid-jp.jp Phase 1 サンプル50件レポート")
    args = parser.parse_args()
    src = ROOT / args.src
    dst = ROOT / (args.dst or f"output/sample_report_{TODAY}.md")
    compare = ROOT / args.compare_with if args.compare_with else None

    records = [json.loads(l) for l in src.open(encoding="utf-8")]
    ok = [r for r in records if not r.get("error")]
    ng = [r for r in records if r.get("error")]
    agg = aggregate(records)
    meta = load_meta(src)

    refs = [r for r in ok if r["source_kind"].startswith("reference")]
    comms = [r for r in ok if not r["source_kind"].startswith("reference")]

    out = []
    out.append(f"# {args.title}")
    out.append("")
    out.append(
        f"生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M')} ／ "
        f"モデル: `{(meta or {}).get('model', 'claude-haiku-4-5-20251001')}`"
    )
    out.append("")
    out.append("## サマリ")
    out.append("")
    out.append(f"- 件数: **{len(records)}件**（成功 {len(ok)} / 失敗 {len(ng)}）")
    out.append(f"  - コミュニティスニペット: **{len(comms)}件**")
    out.append(f"  - 公式リファレンス（theme-liquid-docs）: **{len(refs)}件**")
    if meta:
        out.append(
            f"- 処理時間: {meta.get('elapsed_seconds')}秒（並列 {meta.get('parallel')}）"
        )
    out.append(
        f"- API コスト: **${agg['cost']:.4f}**（入力 {agg['input_tokens']:,} tok ＋ "
        f"出力 {agg['output_tokens']:,} tok"
        + (
            f"、cache_read {agg['cache_read']:,} tok"
            if agg["cache_read"]
            else ""
        )
        + ")"
    )
    out.append("")
    out.append("### カテゴリ分布")
    out.append("")
    out.append("| カテゴリ | 件数 |")
    out.append("|---|---:|")
    for cat, n in agg["categories"].most_common():
        out.append(f"| {cat} | {n} |")
    out.append("")
    out.append("### 難易度分布")
    out.append("")
    out.append("| 難易度 | 件数 |")
    out.append("|---|---:|")
    for d, n in agg["difficulty"].most_common():
        out.append(f"| {d} | {n} |")
    out.append("")
    out.append("### リポジトリ別件数")
    out.append("")
    out.append("| リポジトリ | 件数 |")
    out.append("|---|---:|")
    for repo, n in sorted(agg["by_repo"].items(), key=lambda x: -x[1]):
        out.append(f"| {repo} | {n} |")
    out.append("")
    out.append("## レビュー観点（たけさん向け）")
    out.append("")
    out.append("1. **日本語訳の品質** — 自然な日本語か、誤訳・直訳が残っていないか")
    out.append("2. **カテゴリ分類** — 新カテゴリ体系で適切に分類できているか、誤分類がないか")
    out.append("3. **タイトルフォーマット** — リファレンスは「名前 種別（用途）」、スニペットは「スニペット」「セクション」後置なしを守れているか")
    out.append("4. **タグの命名規則** — 小文字ハイフン区切り・単数形・同義語正規化が効いているか、category と重複していないか")
    out.append(
        "5. **caveats の品質** — 「〜が必要です」連発がないか、①前提→②落とし穴→③応用注意の構成か、具体策が書けているか"
    )
    out.append("6. **include / render 対応** — 原文が include を使っているスニペットで render 推奨の注記が入っているか")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## 📘 公式リファレンス サンプル")
    out.append("")
    for i, r in enumerate(refs, 1):
        out.append(fmt_record(i, r))
        out.append("")
    out.append("---")
    out.append("")
    out.append(f"## 🧩 コミュニティスニペット サンプル（{len(comms)}件）")
    out.append("")
    for i, r in enumerate(comms, 1):
        out.append(fmt_record(i, r))
        out.append("")
    if ng:
        out.append("---")
        out.append("")
        out.append(f"## ❌ 失敗 ({len(ng)}件)")
        out.append("")
        for i, r in enumerate(ng, 1):
            out.append(fmt_record(i, r))

    if compare and compare.exists():
        out.append("---")
        out.append("")
        out.append(build_comparison_section(records, meta, compare))

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n".join(out), encoding="utf-8")
    print(f"[report] wrote -> {dst}", file=sys.stderr)
    print(f"[report] size: {dst.stat().st_size:,} bytes", file=sys.stderr)


if __name__ == "__main__":
    main()
