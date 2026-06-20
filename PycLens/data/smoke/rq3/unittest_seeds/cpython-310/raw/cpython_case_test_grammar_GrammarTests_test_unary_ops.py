# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_unary_ops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = +1
    x = -1
    x = ~1
    x = ~1 ^ 1 & 1 | 1 & 1 ^ -1
    x = -1 * 1 / 1 + 1 * 1 - ---1 * 1
