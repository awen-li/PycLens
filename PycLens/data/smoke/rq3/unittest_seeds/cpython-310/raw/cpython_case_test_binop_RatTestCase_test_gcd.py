# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: RatTestCase_test_gcd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(gcd(10, 12), 2)
    self.assertEqual(gcd(10, 15), 5)
    self.assertEqual(gcd(10, 11), 1)
    self.assertEqual(gcd(100, 15), 5)
    self.assertEqual(gcd(-10, 2), -2)
    self.assertEqual(gcd(10, -2), 2)
    self.assertEqual(gcd(-10, -2), -2)
    for i in range(1, 20):
        for j in range(1, 20):
            self.assertTrue(gcd(i, j) > 0)
            self.assertTrue(gcd(-i, j) < 0)
            self.assertTrue(gcd(i, -j) > 0)
            self.assertTrue(gcd(-i, -j) < 0)
