#!/usr/bin/env bash

PYBCSEC_TOOLS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYBCSEC_TOOLS_ROOT

if [ -x "$PYBCSEC_TOOLS_ROOT/honggfuzz/honggfuzz" ]; then
  export PYBCSEC_HONGGFUZZ_HOME="$(cd "$PYBCSEC_TOOLS_ROOT/honggfuzz" && pwd)"
else
  export PYBCSEC_HONGGFUZZ_HOME="$PYBCSEC_TOOLS_ROOT/pybcSEC/tools"
fi
export PATH="$PYBCSEC_HONGGFUZZ_HOME:$PYBCSEC_HONGGFUZZ_HOME/hfuzz_cc:$PATH"

echo "PYBCSEC_TOOLS_ROOT=$PYBCSEC_TOOLS_ROOT"
echo "PYBCSEC_HONGGFUZZ_HOME=$PYBCSEC_HONGGFUZZ_HOME"
echo "honggfuzz=$(command -v honggfuzz || true)"
