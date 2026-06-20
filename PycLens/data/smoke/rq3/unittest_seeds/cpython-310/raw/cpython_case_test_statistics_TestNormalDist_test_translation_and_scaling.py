# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_translation_and_scaling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    X = NormalDist(100, 15)
    y = 10
    self.assertEqual(+X, NormalDist(100, 15))
    self.assertEqual(-X, NormalDist(-100, 15))
    self.assertEqual(X + y, NormalDist(110, 15))
    self.assertEqual(y + X, NormalDist(110, 15))
    self.assertEqual(X - y, NormalDist(90, 15))
    self.assertEqual(y - X, NormalDist(-90, 15))
    self.assertEqual(X * y, NormalDist(1000, 150))
    self.assertEqual(y * X, NormalDist(1000, 150))
    self.assertEqual(X / y, NormalDist(10, 1.5))
    with self.assertRaises(TypeError):
        y / X
