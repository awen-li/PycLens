# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestSyntaxErrors_test_wildcard_makes_remaining_patterns_unreachable_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assert_syntax_error('\n        match ...:\n            case _:\n                pass\n            case None:\n                pass\n        ')
