#!/usr/bin/env python
"""
build_meili_index.py で生成した JSONL と settings を Meilisearch にバルク投入。
liquid-jp.jp 用の Meilisearch インスタンス(agent-skills.jp と分離した Railway プロジェクト)
を想定するため、環境変数は LIQUID_PROD_MEILI_HOST / LIQUID_PROD_MEILI_MASTER_KEY を優先する。

開発時は MEILI_URL / MEILI_MASTER_KEY (localhost:7700) も可。
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
import meilisearch

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

DEFAULT_INDEX = "liquid_jp"


def get_client(target: str):
    """target = "prod" or "dev" """
    if target == "prod":
        url = os.environ.get("LIQUID_PROD_MEILI_HOST") or os.environ.get("PROD_MEILI_HOST")
        key = os.environ.get("LIQUID_PROD_MEILI_MASTER_KEY") or os.environ.get(
            "PROD_MEILI_MASTER_KEY"
        )
        if not url or not key:
            sys.exit(
                "ERR: LIQUID_PROD_MEILI_HOST / LIQUID_PROD_MEILI_MASTER_KEY が未設定です。"
                "Railway で liquid-jp 用 Meilisearch を起動し、.env に追記してください。"
            )
    else:
        url = os.environ.get("MEILI_URL", "http://localhost:7700")
        key = os.environ.get("MEILI_MASTER_KEY", "")
    print(f"[meili] target={target} url={url}", file=sys.stderr)
    return meilisearch.Client(url, key)


def wait_task(client, task_uid, timeout=120):
    """Meilisearch task を最大 timeout 秒待機"""
    t0 = time.time()
    while time.time() - t0 < timeout:
        info = client.get_task(task_uid)
        status = info.status
        if status in ("succeeded", "failed", "canceled"):
            return status, info
        time.sleep(1)
    return "timeout", None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="meili index jsonl")
    parser.add_argument(
        "--settings",
        default=None,
        help="検索設定 JSON(default: <src>.settings.json)",
    )
    parser.add_argument("--index", default=DEFAULT_INDEX, help="Meilisearch index name")
    parser.add_argument(
        "--target", choices=["dev", "prod"], default="dev", help="dev=localhost:7700, prod=Railway"
    )
    parser.add_argument(
        "--batch-size", type=int, default=500, help="1 リクエストあたりの投入件数"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="既存のインデックスを削除してから作り直す",
    )
    args = parser.parse_args()

    src = ROOT / args.src
    settings_path = (
        ROOT / args.settings
        if args.settings
        else Path(str(src).rsplit(".", 1)[0] + ".settings.json")
    )

    client = get_client(args.target)

    # インデックスのリセット(オプション)
    if args.reset:
        print(f"[meili] reset: deleting index '{args.index}'", file=sys.stderr)
        try:
            task = client.delete_index(args.index)
            wait_task(client, task.task_uid)
        except Exception as e:
            print(f"  (delete skipped: {e})", file=sys.stderr)

    # インデックス作成 or 取得
    try:
        task = client.create_index(args.index, {"primaryKey": "id"})
        wait_task(client, task.task_uid)
    except Exception:
        pass
    index = client.index(args.index)

    # 設定反映
    if settings_path.exists():
        print(f"[meili] applying settings from {settings_path}", file=sys.stderr)
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        task = index.update_settings(settings)
        status, _ = wait_task(client, task.task_uid)
        print(f"  settings task: {status}", file=sys.stderr)
    else:
        print(f"  WARN: settings file not found ({settings_path})", file=sys.stderr)

    # ドキュメント読み込み
    docs = []
    with src.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                docs.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    print(f"[meili] documents to push: {len(docs)}", file=sys.stderr)

    # バッチ投入
    failed = 0
    for i in range(0, len(docs), args.batch_size):
        batch = docs[i: i + args.batch_size]
        task = index.add_documents(batch)
        status, info = wait_task(client, task.task_uid, timeout=180)
        print(
            f"  batch {i + len(batch)}/{len(docs)} task={task.task_uid} status={status}",
            file=sys.stderr,
        )
        if status != "succeeded":
            failed += len(batch)
            if info:
                err = getattr(info, "error", None) or {}
                print(f"    error: {err}", file=sys.stderr)

    # 投入後の件数確認
    stats = index.get_stats()
    print(f"[meili] index stats: {stats}", file=sys.stderr)
    if failed:
        print(f"[meili] WARN: {failed} docs in failed batches", file=sys.stderr)
        sys.exit(1)
    print("[meili] done", file=sys.stderr)


if __name__ == "__main__":
    main()
