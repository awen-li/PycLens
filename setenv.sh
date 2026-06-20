#!/usr/bin/env bash

PYCLENS_TOOLS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYCLENS_TOOLS_ROOT

PYCLENS_HONGGFUZZ_HOME="$(cd "$PYCLENS_TOOLS_ROOT/honggfuzz" && pwd)"
export PYCLENS_HONGGFUZZ_HOME

export PATH="$PYCLENS_HONGGFUZZ_HOME:$PYCLENS_HONGGFUZZ_HOME/hfuzz_cc:$PATH"

echo "PYCLENS_TOOLS_ROOT=$PYCLENS_TOOLS_ROOT"
echo "PYCLENS_HONGGFUZZ_HOME=$PYCLENS_HONGGFUZZ_HOME"
echo "honggfuzz=$(command -v honggfuzz || true)"
