# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ExactRatioTest_test_decimal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    _exact_ratio = statistics._exact_ratio
    self.assertEqual(_exact_ratio(D('0.125')), (1, 8))
    self.assertEqual(_exact_ratio(D('12.345')), (2469, 200))
    self.assertEqual(_exact_ratio(D('-1.98')), (-99, 50))
