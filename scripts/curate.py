#!/usr/bin/env python
"""
Step 1-2: 50件サンプル選定(コミュニティ40 + リファレンス10)。
入力: data/raw_snippets.jsonl
出力: data/sample_50.jsonl
"""
import json
import sys
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "raw_snippets.jsonl"
DST = ROOT / "data" / "sample_50.jsonl"

TARGET_COMMUNITY = 40
TARGET_REFERENCE = 10
PER_REPO_MAX = 6      # 同一リポ偏りを避ける上限
PER_REFKIND = {"filters": 4, "tags": 3, "objects": 3}  # 計 10

# 行数の妥当レンジ(10〜200行優先、不足時は緩和)
PREFERRED_MIN, PREFERRED_MAX = 10, 200


def main():
    records = [json.loads(l) for l in SRC.open(encoding="utf-8")]
    print(f"[select] loaded {len(records)} raw records", file=sys.stderr)

    community = [r for r in records if not r["source_kind"].startswith("reference")]
    references = [r for r in records if r["source_kind"].startswith("reference")]

    # コミュニティ選定: リポ別バケットから順にラウンドロビン
    rng = random.Random(20260513)
    by_repo = defaultdict(list)
    for r in community:
        lines = r["line_count"]
        # 優先レンジを満たすものを上位、外れを下位に
        pref = PREFERRED_MIN <= lines <= PREFERRED_MAX
        r["_priority"] = (0 if pref else 1, lines)
        by_repo[r["repo_name"]].append(r)
    for repo in by_repo:
        by_repo[repo].sort(key=lambda x: x["_priority"])
        rng.shuffle(by_repo[repo])  # 同 priority 内ランダム
        by_repo[repo].sort(key=lambda x: x["_priority"])

    selected_comm = []
    repo_taken = defaultdict(int)
    # ラウンドロビン: 各リポから1件ずつ取る、PER_REPO_MAX まで
    repos = list(by_repo.keys())
    rng.shuffle(repos)
    while len(selected_comm) < TARGET_COMMUNITY:
        progress = False
        for repo in repos:
            if len(selected_comm) >= TARGET_COMMUNITY:
                break
            if repo_taken[repo] >= PER_REPO_MAX:
                continue
            if repo_taken[repo] < len(by_repo[repo]):
                selected_comm.append(by_repo[repo][repo_taken[repo]])
                repo_taken[repo] += 1
                progress = True
        if not progress:
            break

    # リファレンス選定: kind 別に均等
    by_kind = defaultdict(list)
    for r in references:
        k = r.get("reference_kind", r["source_kind"].replace("reference-", ""))
        by_kind[k].append(r)
    selected_ref = []
    for kind, n in PER_REFKIND.items():
        bucket = by_kind.get(kind, [])
        rng.shuffle(bucket)
        selected_ref.extend(bucket[:n])

    sample = selected_comm + selected_ref
    print(
        f"[select] community={len(selected_comm)} reference={len(selected_ref)} "
        f"total={len(sample)}",
        file=sys.stderr,
    )

    # 統計
    repo_dist = defaultdict(int)
    for r in selected_comm:
        repo_dist[r["repo_name"]] += 1
    print("[select] community by repo:", file=sys.stderr)
    for repo, n in sorted(repo_dist.items(), key=lambda x: -x[1]):
        print(f"  {repo}: {n}", file=sys.stderr)
    kind_dist = defaultdict(int)
    for r in selected_ref:
        kind_dist[r.get("reference_kind", "?")] += 1
    print("[select] reference by kind:", file=sys.stderr)
    for k, n in kind_dist.items():
        print(f"  {k}: {n}", file=sys.stderr)

    # 出力(_priority は除去)
    with DST.open("w", encoding="utf-8") as fout:
        for r in sample:
            r.pop("_priority", None)
            fout.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"[select] wrote {len(sample)} -> {DST}", file=sys.stderr)


if __name__ == "__main__":
    main()
