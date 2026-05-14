#!/usr/bin/env python
"""
B3: title-too-long タグ付き 128件を A/B/C に自動仕分け。
- A: 30字以内に短縮可能(AI が短縮版を返す) → translated_full.jsonl に自動反映
- B: 短縮困難(AI が DIFFICULT を返す or 短縮版も30字超え)
- C: 判断保留(AI が DEFER を返す)

出力:
- 元の translated_full.jsonl を上書き(A適用後)
- docs/title_review.md (A適用後/B理由/C一覧)
"""
import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

MODEL = "claude-haiku-4-5-20251001"
PARALLEL = 8
TITLE_MAX = 30

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


SYSTEM_PROMPT = """あなたは Shopify Liquid カタログの編集者です。
ユーザーから提示された日本語タイトルを、意味を保ったまま 30字以内に短縮します。

# ルール
- リファレンス系タイトルは「{name} フィルター（用途）」「{name} タグ（用途）」「{name} オブジェクト」の形式
- スニペット系タイトルは「30字以内の機能名のみ」(末尾の「スニペット」「セクション」「ブロック」は禁止)
- 用途を端的に表す日本語に短縮する
- 並列構造（A・B・C・D の列挙）は維持できない場合のみ削るか抽象化する
- 重要なキーワード(オブジェクト名、フィルター名、機能名)は残す

# 出力形式(厳守)
- 短縮できる場合: 短縮タイトル1行のみ(クオート禁止、前置き禁止、コードフェンス禁止)
- 並列構造などで意味を保ったまま 30字以内に収めるのが困難な場合: "DIFFICULT: 理由(20字以内)"
- 元タイトルの意図が読み取れない、判断に迷う場合: "DEFER: 理由(20字以内)"
"""


def curate_title(rec_id: str, original_title: str, file_name: str):
    """1件分の短縮提案を AI に依頼"""
    user_msg = f"""元タイトル(全 {len(original_title)} 字): {original_title}
ファイル名(参考): {file_name}

30字以内に短縮してください。"""
    try:
        resp = client.messages.create(
            model=MODEL,
            max_tokens=80,
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": user_msg}],
        )
        text = "".join(b.text for b in resp.content if hasattr(b, "text")).strip()
        usage = resp.usage
        return {
            "id": rec_id,
            "original": original_title,
            "ai_response": text,
            "usage": {
                "in": usage.input_tokens,
                "out": usage.output_tokens,
                "cache_create": getattr(usage, "cache_creation_input_tokens", 0),
                "cache_read": getattr(usage, "cache_read_input_tokens", 0),
            },
            "error": None,
        }
    except Exception as e:
        return {
            "id": rec_id,
            "original": original_title,
            "ai_response": "",
            "usage": None,
            "error": str(e),
        }


def classify(result: dict):
    """AI 応答を A/B/C に分類"""
    text = (result.get("ai_response") or "").strip()
    original = result["original"]
    if result.get("error"):
        return {"cls": "C", "new_title": original, "reason": f"AI error: {result['error']}"}
    if not text:
        return {"cls": "C", "new_title": original, "reason": "empty AI response"}
    if text.startswith("DIFFICULT:"):
        return {"cls": "B", "new_title": original, "reason": text[10:].strip() or "短縮困難"}
    if text.startswith("DEFER:"):
        return {"cls": "C", "new_title": original, "reason": text[6:].strip() or "判断保留"}
    # 前後のクオート除去
    candidate = text.strip("\"'「」 　\n")
    if len(candidate) > TITLE_MAX:
        return {
            "cls": "B",
            "new_title": original,
            "reason": f"AI 短縮版も {len(candidate)} 字: {candidate}",
        }
    if len(candidate) < 4:
        return {
            "cls": "C",
            "new_title": original,
            "reason": f"短縮版が短すぎる({len(candidate)}字): {candidate}",
        }
    return {"cls": "A", "new_title": candidate, "reason": ""}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="data/translated_full.jsonl")
    parser.add_argument("--out-md", default="docs/title_review.md")
    args = parser.parse_args()
    src = ROOT / args.src
    md_out = ROOT / args.out_md
    md_out.parent.mkdir(parents=True, exist_ok=True)

    # 全レコード読み込み
    records = []
    with src.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    targets = []
    for r in records:
        tags = ((r.get("translation") or {}).get("tags") or [])
        if "title-too-long" in tags:
            targets.append(r)
    print(f"[curate] title-too-long: {len(targets)} 件", file=sys.stderr)

    # AI 短縮提案を並列取得
    results = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=PARALLEL) as pool:
        futures = {
            pool.submit(
                curate_title,
                r["id"],
                (r["translation"] or {}).get("title_ja", ""),
                r.get("file_name", ""),
            ): r["id"]
            for r in targets
        }
        for n, fut in enumerate(as_completed(futures), 1):
            res = fut.result()
            results.append(res)
            if n % 20 == 0 or n == len(targets):
                print(f"  [{n:>3}/{len(targets)}]", file=sys.stderr)
    elapsed = time.time() - t0

    # 分類
    by_id = {res["id"]: classify(res) for res in results}

    # translated_full.jsonl に A を反映
    a_count = b_count = c_count = 0
    applied: list = []
    updated_records = []
    for r in records:
        rid = r["id"]
        if rid not in by_id:
            updated_records.append(r)
            continue
        info = by_id[rid]
        cls = info["cls"]
        if cls == "A":
            old = (r["translation"] or {}).get("title_ja", "")
            r["translation"]["title_ja"] = info["new_title"]
            # title-too-long タグを除去(30字以内になったので)
            tags = r["translation"].get("tags", []) or []
            r["translation"]["tags"] = [t for t in tags if t != "title-too-long"]
            applied.append({"id": rid, "before": old, "after": info["new_title"]})
            a_count += 1
        elif cls == "B":
            b_count += 1
        elif cls == "C":
            c_count += 1
        updated_records.append(r)

    # backup + 上書き
    bak = src.with_suffix(".jsonl.before_curate.bak")
    src.rename(bak)
    with src.open("w", encoding="utf-8") as f:
        for r in updated_records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(
        f"[curate] backup -> {bak.name}, overwrote -> {src.name}",
        file=sys.stderr,
    )

    # Markdown レポート
    lines = ["# Phase 3 ブロック3: title_too_long 自動仕分け", ""]
    lines.append(f"対象: {len(targets)} 件 / 所要 {elapsed:.1f}秒 / モデル {MODEL}")
    lines.append("")
    lines.append(f"- **A: 短縮適用** … **{a_count}件**(自動で `title_ja` を更新、`title-too-long` タグ除去)")
    lines.append(f"- **B: 短縮困難で維持** … **{b_count}件**")
    lines.append(f"- **C: 人間レビュー対象** … **{c_count}件**")
    lines.append("")

    # A 適用一覧
    lines.append("## A: 短縮適用済み")
    lines.append("")
    lines.append("| # | Before(字数) | After(字数) | id |")
    lines.append("|---:|---|---|---|")
    for i, ap in enumerate(applied, 1):
        lines.append(
            f"| {i} | {ap['before']} ({len(ap['before'])}) | "
            f"**{ap['after']}** ({len(ap['after'])}) | `{ap['id']}` |"
        )
    lines.append("")

    # B 維持理由
    bs = [
        {"id": rid, "title": (next(r for r in records if r["id"] == rid).get("translation") or {}).get("title_ja", ""), "reason": info["reason"]}
        for rid, info in by_id.items() if info["cls"] == "B"
    ]
    lines.append(f"## B: 維持(短縮困難) — {len(bs)}件")
    lines.append("")
    lines.append("| # | タイトル(字数) | 理由 | id |")
    lines.append("|---:|---|---|---|")
    for i, b in enumerate(bs, 1):
        lines.append(f"| {i} | {b['title']} ({len(b['title'])}) | {b['reason']} | `{b['id']}` |")
    lines.append("")

    # C 一覧
    cs = [
        {"id": rid, "title": (next(r for r in records if r["id"] == rid).get("translation") or {}).get("title_ja", ""), "reason": info["reason"]}
        for rid, info in by_id.items() if info["cls"] == "C"
    ]
    lines.append(f"## C: 人間レビュー対象 — {len(cs)}件")
    lines.append("")
    lines.append("| # | タイトル(字数) | 理由 | id |")
    lines.append("|---:|---|---|---|")
    for i, c in enumerate(cs, 1):
        lines.append(f"| {i} | {c['title']} ({len(c['title'])}) | {c['reason']} | `{c['id']}` |")
    lines.append("")

    # コスト集計
    in_tok = sum((res.get("usage") or {}).get("in", 0) for res in results)
    out_tok = sum((res.get("usage") or {}).get("out", 0) for res in results)
    cache_create = sum((res.get("usage") or {}).get("cache_create", 0) for res in results)
    cache_read = sum((res.get("usage") or {}).get("cache_read", 0) for res in results)
    total_input = in_tok + cache_create + cache_read
    hit_rate = (cache_read / total_input) if total_input else 0.0
    cost = (
        in_tok / 1_000_000
        + out_tok * 5 / 1_000_000
        + cache_create * 1.25 / 1_000_000
        + cache_read * 0.1 / 1_000_000
    )
    lines.append("## メタ")
    lines.append("")
    lines.append(f"- 入力 tokens: {in_tok:,} / 出力 tokens: {out_tok:,}")
    lines.append(f"- cache create: {cache_create:,} / cache read: {cache_read:,}")
    lines.append(f"- cache_hit_rate: {hit_rate*100:.1f}%")
    lines.append(f"- 推定コスト: **${cost:.4f}**")

    md_out.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"\n[curate] A={a_count} B={b_count} C={c_count} cost=${cost:.4f} hit_rate={hit_rate*100:.1f}%",
        file=sys.stderr,
    )
    print(f"[curate] report -> {md_out}", file=sys.stderr)
    # JSON サイドカー
    sidecar = md_out.with_suffix(".json")
    sidecar.write_text(
        json.dumps(
            {
                "A": [ap for ap in applied],
                "B": bs,
                "C": cs,
                "total": len(targets),
                "elapsed_seconds": round(elapsed, 1),
                "cost_usd": round(cost, 6),
                "cache_hit_rate": round(hit_rate, 4),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"[curate] sidecar json -> {sidecar}", file=sys.stderr)


if __name__ == "__main__":
    main()
