# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_nan_inf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(OverflowError, int, float('inf'))
    self.assertRaises(OverflowError, int, float('-inf'))
    self.assertRaises(ValueError, int, float('nan'))
