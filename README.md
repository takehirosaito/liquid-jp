# liquid-jp.jp

Shopify Liquid スニペットの日本語カタログサイト。ALSEL「翻訳アービトラージ」第2弾、[agent-skills.jp](https://agent-skills.jp) の Liquid 版。

## 方針

- ドメイン: `liquid-jp.jp`
- データ源ライセンス: **MIT / CC0 / Apache 2.0 / BSD のみ採用**（Dawn / Horizon は完全除外）
- 構造: 公式リファレンス（theme-liquid-docs 日本語版）+ コミュニティスニペット集 のハイブリッド
- 検索: Meilisearch（Railway 上、agent-skills.jp とは別インスタンス）

詳細は `~/.claude/projects/-Users-takehirosaito/memory/project_liquid_jp.md` 参照。

## ディレクトリ

```
liquid-jp/
├── scripts/        # fetch / select / translate / report
├── data/           # JSONL（生データ・選定済み・翻訳済み）
├── output/         # Markdown レポート
└── .env -> ~/agent-skills.jp/agent-skills-jp/.env （API キー共有）
```

## Phase 1 実行（ステップ1-2）

```bash
PYTHON=/Users/takehirosaito/agent-skills.jp/agent-skills-jp/.venv/bin/python
$PYTHON scripts/fetch.py       # 200件取得 → data/raw_snippets.jsonl
$PYTHON scripts/curate.py      # 50件選定 → data/sample_50.jsonl
$PYTHON scripts/translate.py   # 日本語化 → data/translated_50.jsonl
$PYTHON scripts/report.py      # レポート → output/sample_report_YYYYMMDD.md
```
