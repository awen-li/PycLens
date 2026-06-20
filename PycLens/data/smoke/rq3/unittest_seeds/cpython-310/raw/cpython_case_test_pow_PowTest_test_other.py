# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pow.py
# case: PowTest_test_other

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pow(3, 3) % 8, pow(3, 3, 8))
    self.assertEqual(pow(3, 3) % -8, pow(3, 3, -8))
    self.assertEqual(pow(3, 2) % -2, pow(3, 2, -2))
    self.assertEqual(pow(-3, 3) % 8, pow(-3, 3, 8))
    self.assertEqual(pow(-3, 3) % -8, pow(-3, 3, -8))
    self.assertEqual(pow(5, 2) % -8, pow(5, 2, -8))
    self.assertEqual(pow(3, 3) % 8, pow(3, 3, 8))
    self.assertEqual(pow(3, 3) % -8, pow(3, 3, -8))
    self.assertEqual(pow(3, 2) % -2, pow(3, 2, -2))
    self.assertEqual(pow(-3, 3) % 8, pow(-3, 3, 8))
    self.assertEqual(pow(-3, 3) % -8, pow(-3, 3, -8))
    self.assertEqual(pow(5, 2) % -8, pow(5, 2, -8))
    for i in range(-10, 11):
        for j in range(0, 6):
            for k in range(-7, 11):
                if j >= 0 and k != 0:
                    self.assertEqual(pow(i, j) % k, pow(i, j, k))
                if j >= 0 and k != 0:
                    self.assertEqual(pow(int(i), j) % k, pow(int(i), j, k))
