#!/usr/bin/env bash

PYCLENS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYCLENS_ROOT

PYCLENS_PYLINGUAL_HOME="$PYCLENS_ROOT/data/rq2/envs/global-pylingual"
export PYCLENS_PYLINGUAL_HOME

PYCLENS_HONGGFUZZ_HOME="$PYCLENS_ROOT/honggfuzz"
export PYCLENS_HONGGFUZZ_HOME

export PATH="$PYCLENS_PYLINGUAL_HOME/bin:$PYCLENS_HONGGFUZZ_HOME:$PYCLENS_HONGGFUZZ_HOME/hfuzz_cc:$PATH"

echo "PYCLENS_ROOT=$PYCLENS_ROOT"
echo "PYCLENS_PYLINGUAL_HOME=$PYCLENS_PYLINGUAL_HOME"
echo "PYCLENS_HONGGFUZZ_HOME=$PYCLENS_HONGGFUZZ_HOME"
echo "pylingual=$(command -v pylingual || true)"
echo "honggfuzz=$(command -v honggfuzz || true)"
