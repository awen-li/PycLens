# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestStdev_test_single_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (81, 203.74, 390000000000000.0, Fraction(5, 21), Decimal('35.719')):
        self.assertRaises(statistics.StatisticsError, self.func, [x])
