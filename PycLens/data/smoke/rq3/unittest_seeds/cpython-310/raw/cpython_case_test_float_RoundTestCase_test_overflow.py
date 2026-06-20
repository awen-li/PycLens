# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(OverflowError, round, 1.6e+308, -308)
    self.assertRaises(OverflowError, round, -1.7e+308, -308)
