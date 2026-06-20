# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: DecimalToRatioTest_test_positive_exponent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = statistics._exact_ratio(Decimal('1.234e7'))
    self.assertEqual(t, (12340000, 1))
