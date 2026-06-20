# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestVariance_test_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    data = [D(2), D(2), D(7), D(9)]
    exact = 4 * D('9.5') / D(3)
    result = self.func(data)
    self.assertEqual(result, exact)
    self.assertIsInstance(result, Decimal)
