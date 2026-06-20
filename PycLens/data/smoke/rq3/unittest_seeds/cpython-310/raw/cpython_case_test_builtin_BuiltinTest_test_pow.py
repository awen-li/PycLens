# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_pow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pow(0, 0), 1)
    self.assertEqual(pow(0, 1), 0)
    self.assertEqual(pow(1, 0), 1)
    self.assertEqual(pow(1, 1), 1)
    self.assertEqual(pow(2, 0), 1)
    self.assertEqual(pow(2, 10), 1024)
    self.assertEqual(pow(2, 20), 1024 * 1024)
    self.assertEqual(pow(2, 30), 1024 * 1024 * 1024)
    self.assertEqual(pow(-2, 0), 1)
    self.assertEqual(pow(-2, 1), -2)
    self.assertEqual(pow(-2, 2), 4)
    self.assertEqual(pow(-2, 3), -8)
    self.assertAlmostEqual(pow(0.0, 0), 1.0)
    self.assertAlmostEqual(pow(0.0, 1), 0.0)
    self.assertAlmostEqual(pow(1.0, 0), 1.0)
    self.assertAlmostEqual(pow(1.0, 1), 1.0)
    self.assertAlmostEqual(pow(2.0, 0), 1.0)
    self.assertAlmostEqual(pow(2.0, 10), 1024.0)
    self.assertAlmostEqual(pow(2.0, 20), 1024.0 * 1024.0)
    self.assertAlmostEqual(pow(2.0, 30), 1024.0 * 1024.0 * 1024.0)
    self.assertAlmostEqual(pow(-2.0, 0), 1.0)
    self.assertAlmostEqual(pow(-2.0, 1), -2.0)
    self.assertAlmostEqual(pow(-2.0, 2), 4.0)
    self.assertAlmostEqual(pow(-2.0, 3), -8.0)
    for x in (2, 2.0):
        for y in (10, 10.0):
            for z in (1000, 1000.0):
                if isinstance(x, float) or isinstance(y, float) or isinstance(z, float):
                    self.assertRaises(TypeError, pow, x, y, z)
                else:
                    self.assertAlmostEqual(pow(x, y, z), 24.0)
    self.assertAlmostEqual(pow(-1, 0.5), 1j)
    self.assertAlmostEqual(pow(-1, 1 / 3), 0.5 + 0.8660254037844386j)
    self.assertEqual(pow(-1, -2, 3), 1)
    self.assertRaises(ValueError, pow, 1, 2, 0)
    self.assertRaises(TypeError, pow)
    self.assertEqual(pow(0, exp=0), 1)
    self.assertEqual(pow(base=2, exp=4), 16)
    self.assertEqual(pow(base=5, exp=2, mod=14), 11)
    twopow = partial(pow, base=2)
    self.assertEqual(twopow(exp=5), 32)
    fifth_power = partial(pow, exp=5)
    self.assertEqual(fifth_power(2), 32)
    mod10 = partial(pow, mod=10)
    self.assertEqual(mod10(2, 6), 4)
    self.assertEqual(mod10(exp=6, base=2), 4)
