# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: DecimalToRatioTest_test_infinity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inf = Decimal('INF')
    self.assertEqual(statistics._exact_ratio(inf), (inf, None))
    self.assertEqual(statistics._exact_ratio(-inf), (-inf, None))
