#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOL_DIR="$ROOT_DIR/PycLens"
HONGGFUZZ_HOME="$ROOT_DIR/honggfuzz"

echo "[buildtool] build honggfuzz"
make -C "$HONGGFUZZ_HOME" -j "$(nproc)"

echo "[buildtool] install PycLens"
python3 -m pip install -e "$TOOL_DIR"

echo "[buildtool] check PycLens"
pyclens --help >/dev/null

echo "[buildtool] done"
