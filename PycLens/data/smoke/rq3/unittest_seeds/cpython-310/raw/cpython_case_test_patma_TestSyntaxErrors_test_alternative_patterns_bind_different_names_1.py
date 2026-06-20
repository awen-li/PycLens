# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestSyntaxErrors_test_alternative_patterns_bind_different_names_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assert_syntax_error('\n        match ...:\n            case [a, [b] | [c] | [d]]:\n                pass\n        ')
