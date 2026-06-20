# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestVariance_test_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    F = Fraction
    data = [F(1, 4), F(1, 4), F(3, 4), F(7, 4)]
    exact = F(1, 2)
    result = self.func(data)
    self.assertEqual(result, exact)
    self.assertIsInstance(result, Fraction)
