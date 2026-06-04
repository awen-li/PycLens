#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOL_DIR="$ROOT_DIR/tools/pybcSEC"
HONGGFUZZ_HOME="$ROOT_DIR/tools/honggfuzz"
HONGGFUZZ="$HONGGFUZZ_HOME/honggfuzz"

echo "[buildtool] installing pybcSEC from $TOOL_DIR"
python3 -m pip install -e "$TOOL_DIR"

echo "[buildtool] checking pybcSEC command"
pybcSEC --help >/dev/null

if [ -f "$HONGGFUZZ" ]; then
  chmod +x "$HONGGFUZZ"
  echo "[buildtool] honggfuzz found at $HONGGFUZZ"
else
  echo "[buildtool] honggfuzz not found at $HONGGFUZZ"
  echo "[buildtool] RQ3 fuzzing will require source tools/setenv.sh after honggfuzz is built"
fi

echo "[buildtool] done"
