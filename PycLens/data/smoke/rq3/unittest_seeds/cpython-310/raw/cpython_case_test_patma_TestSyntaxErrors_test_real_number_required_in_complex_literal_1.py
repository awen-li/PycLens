# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestSyntaxErrors_test_real_number_required_in_complex_literal_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assert_syntax_error('\n        match ...:\n            case 0j+0j:\n                pass\n        ')
