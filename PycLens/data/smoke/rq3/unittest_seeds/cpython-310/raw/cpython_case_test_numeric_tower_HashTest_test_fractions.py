# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: HashTest_test_fractions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(hash(F(1, _PyHASH_MODULUS)), _PyHASH_INF)
    self.assertEqual(hash(F(-1, 3 * _PyHASH_MODULUS)), -_PyHASH_INF)
    self.assertEqual(hash(F(7 * _PyHASH_MODULUS, 1)), 0)
    self.assertEqual(hash(F(-_PyHASH_MODULUS, 1)), 0)
    x = F(DummyIntegral(1), DummyIntegral(2), _normalize=False)
    self.assertRaises(TypeError, lambda : x.numerator / x.denominator)
    self.assertEqual(float(x), 0.5)
