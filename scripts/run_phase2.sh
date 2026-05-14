#!/usr/bin/env bash
# Phase 2 完走スクリプト: translate → style_check → build_meili → push_to_meili → report
# 任意のステップでエラーが出たら停止し、状態を logs/phase2_status_<DATE>.json に残す。

set -uo pipefail  # set -e は run_step 内で明示制御

cd "$(dirname "$0")/.."  # ~/liquid-jp に移動
ROOT=$(pwd)
PYTHON=/Users/takehirosaito/agent-skills.jp/agent-skills-jp/.venv/bin/python
DATE="${1:-$(date +%Y%m%d_%H%M)}"
mkdir -p logs

LOG_RUN="logs/phase2_run_${DATE}.log"
STATUS="logs/phase2_status_${DATE}.json"

ts() { date "+%Y-%m-%d %H:%M:%S"; }
log() { echo "[$(ts)] $*" | tee -a "$LOG_RUN"; }

write_status() {
    # $1: status (running / succeeded / failed)
    # $2: optional JSON 追加プロパティ(先頭 , 込み)
    local st=$1
    local extra=${2:-}
    cat > "$STATUS" <<EOF
{
  "status": "$st",
  "updated_at": "$(date +%FT%T%z)",
  "date_token": "$DATE",
  "log_run": "$LOG_RUN"$extra
}
EOF
}

run_step() {
    local name=$1
    local logfile=$2
    shift 2
    log "=== STEP $name START ==="
    if ! "$@" > "$logfile" 2>&1; then
        local rc=$?
        log "=== STEP $name FAILED (rc=$rc) ==="
        log "--- tail of $logfile ---"
        tail -30 "$logfile" | sed 's/^/    /' | tee -a "$LOG_RUN" >/dev/null
        write_status "failed" ",
  \"failed_step\": \"$name\",
  \"failed_rc\": $rc,
  \"failed_log\": \"$logfile\""
        exit "$rc"
    fi
    log "=== STEP $name OK ==="
}

write_status "running" ",
  \"started_at\": \"$(date +%FT%T%z)\""

log "Phase 2 連鎖実行開始 (DATE=$DATE)"
log "PYTHON=$PYTHON"
log "ROOT=$ROOT"

# Step 2: translate
run_step "translate" "logs/translate_${DATE}.log" \
    "$PYTHON" scripts/translate.py \
    --src data/raw_full.jsonl --dst data/translated_full.jsonl

# Step 3: style_check (違反検出は exit 0、品質ゲートはあくまで情報として)
run_step "style_check" "logs/style_${DATE}.log" \
    "$PYTHON" scripts/style_check.py \
    --files data/translated_full.jsonl --labels phase2

# Step 4: build_meili
run_step "build_meili" "logs/build_${DATE}.log" \
    "$PYTHON" scripts/build_meili_index.py \
    --src data/translated_full.jsonl --out data/meili_index.jsonl

# Step 5: push_to_meili (本番 Railway、reset 付き)
run_step "push_meili" "logs/push_${DATE}.log" \
    "$PYTHON" scripts/push_to_meili.py \
    --src data/meili_index.jsonl --index liquid_jp --target prod --reset

# Step 6: report
run_step "report" "logs/report_${DATE}.log" \
    "$PYTHON" scripts/report.py \
    --src data/translated_full.jsonl --dst docs/phase2-full.md

write_status "succeeded" ",
  \"finished_at\": \"$(date +%FT%T%z)\""
log "=== ALL STEPS DONE ==="
