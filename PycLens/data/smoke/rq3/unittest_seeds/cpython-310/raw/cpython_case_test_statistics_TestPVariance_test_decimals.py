# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestPVariance_test_decimals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = Decimal
    data = [D('12.1'), D('12.2'), D('12.5'), D('12.9')]
    exact = D('0.096875')
    result = self.func(data)
    self.assertEqual(result, exact)
    self.assertIsInstance(result, Decimal)
