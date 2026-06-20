# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pow.py
# case: PowTest_test_negative_exponent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for a in range(-50, 50):
        for m in range(-50, 50):
            with self.subTest(a=a, m=m):
                if m != 0 and math.gcd(a, m) == 1:
                    inv = pow(a, -1, m)
                    self.assertEqual(inv, inv % m)
                    self.assertEqual((inv * a - 1) % m, 0)
                    self.assertEqual(pow(a, -2, m), pow(inv, 2, m))
                    self.assertEqual(pow(a, -3, m), pow(inv, 3, m))
                    self.assertEqual(pow(a, -1001, m), pow(inv, 1001, m))
                else:
                    with self.assertRaises(ValueError):
                        pow(a, -1, m)
                    with self.assertRaises(ValueError):
                        pow(a, -2, m)
                    with self.assertRaises(ValueError):
                        pow(a, -1001, m)
