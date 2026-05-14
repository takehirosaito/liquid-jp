#!/usr/bin/env python
"""
日本語スタイルルールに対する違反件数をスキャン。
v3 / v4 比較や Phase 2 起動前のチェックに使う。
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEXT_FIELDS = (
    "title_ja",
    "description_ja",
    "use_case_ja",
    "where_to_paste_ja",
    "caveats_ja",
)
JP_GAP_RE = re.compile(r"[ぁ-んァ-ヶー一-龯々]\s+[ぁ-んァ-ヶー一-龯々]")
HAS_JP_RE = re.compile(r"[ぁ-んァ-ヶー一-龯々]")
PAREN_RE = re.compile(r"\(([^()]*)\)")

# たけさんの15件表に対応するルール
RULES = [
    ("1.  記号連続列挙 (&<> など読点なし)", re.compile(r"\(\s*&[<>][<>&]")),
    ("2.  敬体 '〜します' (常体違反)", re.compile(r"(?:します|します。|します、|します$|します　)")),
    ("3.  'データ層' (漠然)", re.compile(r"データ層")),
    ("4.  '展開収縮' / '展開縮小'", re.compile(r"展開収縮|展開縮小")),
    ("6.  'hardcoded' (英単語混在)", re.compile(r"\bhardcoded\b")),
    ("7.  'break する' (カジュアル)", re.compile(r"break\s*する")),
    ("11. 'API的' (中途半端)", re.compile(r"API\s*的")),
    ("12. '液体' (Liquid 誤訳)", re.compile(r"液体(?!窒素|酸素|水素|クロマト|燃料)")),
    ("14. '〜ことを通知' (主語曖昧)", re.compile(r"ことを通知")),
    ("15. 'Web に' / 'Web で' (中途半端、上を除外)", re.compile(r"Web\s*[にで](?!上)")),
]


def iter_texts(records):
    for r in records:
        t = r.get("translation") or {}
        for k in TEXT_FIELDS:
            v = t.get(k)
            if isinstance(v, str):
                yield (r["id"], k, v)


def count_jp_gap(records):
    hits = []
    for rid, field, text in iter_texts(records):
        if JP_GAP_RE.search(text):
            # 該当箇所抜粋(前後10字)
            m = JP_GAP_RE.search(text)
            s, e = m.span()
            ctx = text[max(0, s - 10): e + 10]
            hits.append((rid, field, ctx))
    return hits


def count_paren_jp(records):
    """日本語を含む半角括弧の混在"""
    hits = []
    for rid, field, text in iter_texts(records):
        for m in PAREN_RE.finditer(text):
            content = m.group(1)
            if HAS_JP_RE.search(content):
                hits.append((rid, field, m.group(0)))
                break
    return hits


def scan(records, label):
    print(f"\n{'=' * 70}")
    print(f"  {label} ({len(records)}件)")
    print("=" * 70)
    counts = {}
    for rule_label, pat in RULES:
        hits = []
        for rid, field, text in iter_texts(records):
            if pat.search(text):
                m = pat.search(text)
                s, e = m.span()
                ctx = text[max(0, s - 15): e + 15]
                hits.append((rid, field, ctx))
        counts[rule_label] = len(hits)
        marker = "OK " if not hits else "NG "
        print(f"[{marker}] {rule_label}: {len(hits)} 件")
        for h in hits[:2]:
            print(f"       例: …{h[2]}…  [{h[0]}/{h[1]}]")

    # 8-10. 日本語間スペース
    jp_gap_hits = count_jp_gap(records)
    counts["8-10. 日本語間スペース"] = len(jp_gap_hits)
    marker = "OK " if not jp_gap_hits else "NG "
    print(f"[{marker}] 8-10. 日本語間スペース: {len(jp_gap_hits)} 件")
    for h in jp_gap_hits[:2]:
        print(f"       例: …{h[2]}…  [{h[0]}/{h[1]}]")

    # 5. 半角括弧で日本語混在
    paren_hits = count_paren_jp(records)
    counts["5.  半角括弧で日本語混在"] = len(paren_hits)
    marker = "OK " if not paren_hits else "NG "
    print(f"[{marker}] 5. 半角括弧で日本語混在: {len(paren_hits)} 件")
    for h in paren_hits[:2]:
        print(f"       例: {h[2]}  [{h[0]}/{h[1]}]")

    total = sum(counts.values())
    print(f"\n  ===> 合計違反: {total} 件")
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True, help="path(s) to translated_*.jsonl")
    parser.add_argument("--labels", nargs="+", help="labels matching each file (e.g. v3 v4)")
    args = parser.parse_args()

    labels = args.labels or [Path(f).stem for f in args.files]
    if len(labels) != len(args.files):
        print("ERR: --labels count must match --files count", file=sys.stderr)
        sys.exit(1)

    summary = {}
    for path, label in zip(args.files, labels):
        records = [json.loads(l) for l in (ROOT / path).open(encoding="utf-8")]
        counts = scan(records, label)
        summary[label] = counts

    # 比較サマリ
    if len(summary) >= 2:
        print(f"\n{'=' * 70}")
        print(f"  比較サマリ: {' vs '.join(summary.keys())}")
        print("=" * 70)
        all_rules = list(next(iter(summary.values())).keys())
        header_labels = "  ".join(f"{l:>6}" for l in summary)
        print(f"{'ルール':50s} {header_labels}")
        print("-" * 78)
        for rule in all_rules:
            row = "  ".join(f"{summary[l].get(rule, 0):>6}" for l in summary)
            print(f"{rule:50s} {row}")
        totals = {l: sum(c.values()) for l, c in summary.items()}
        row = "  ".join(f"{totals[l]:>6}" for l in summary)
        print("-" * 78)
        print(f"{'合計':50s} {row}")


if __name__ == "__main__":
    main()
