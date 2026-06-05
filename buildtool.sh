#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOL_DIR="$ROOT_DIR/tools/pybcSEC"
HONGGFUZZ_HOME="$ROOT_DIR/tools/honggfuzz"

echo "[buildtool] build honggfuzz"
make -C "$HONGGFUZZ_HOME" -j "$(nproc)"

echo "[buildtool] install pybcSEC"
python3 -m pip install -e "$TOOL_DIR"

echo "[buildtool] check pybcSEC"
pybcSEC --help >/dev/null

echo "[buildtool] done"
