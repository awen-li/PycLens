# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestMultipleArgs_test_nargs_invalid_float_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseFail(['-p', '1.0', '2x', '3.5'], "option -p: invalid floating-point value: '2x'")
