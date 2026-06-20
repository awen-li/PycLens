# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_rounding_strings_interned

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(C.ROUND_UP, P.ROUND_UP)
    self.assertIs(C.ROUND_DOWN, P.ROUND_DOWN)
    self.assertIs(C.ROUND_CEILING, P.ROUND_CEILING)
    self.assertIs(C.ROUND_FLOOR, P.ROUND_FLOOR)
    self.assertIs(C.ROUND_HALF_UP, P.ROUND_HALF_UP)
    self.assertIs(C.ROUND_HALF_DOWN, P.ROUND_HALF_DOWN)
    self.assertIs(C.ROUND_HALF_EVEN, P.ROUND_HALF_EVEN)
    self.assertIs(C.ROUND_05UP, P.ROUND_05UP)
