# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestVariance_test_single_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (35, 24.7, 8200000000000000.0, Fraction(19, 30), Decimal('4.2084')):
        self.assertRaises(statistics.StatisticsError, self.func, [x])
