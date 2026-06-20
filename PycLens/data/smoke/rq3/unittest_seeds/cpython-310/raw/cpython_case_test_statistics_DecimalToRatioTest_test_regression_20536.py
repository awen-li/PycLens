# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: DecimalToRatioTest_test_regression_20536

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = statistics._exact_ratio(Decimal('1e2'))
    self.assertEqual(t, (100, 1))
    t = statistics._exact_ratio(Decimal('1.47e5'))
    self.assertEqual(t, (147000, 1))
