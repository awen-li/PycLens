# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_pow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAlmostEqual(pow(1 + 1j, 0 + 0j), 1.0)
    self.assertAlmostEqual(pow(0 + 0j, 2 + 0j), 0.0)
    self.assertRaises(ZeroDivisionError, pow, 0 + 0j, 1j)
    self.assertAlmostEqual(pow(1j, -1), 1 / 1j)
    self.assertAlmostEqual(pow(1j, 200), 1)
    self.assertRaises(ValueError, pow, 1 + 1j, 1 + 1j, 1 + 1j)
    self.assertRaises(OverflowError, pow, 1e+200 + 1j, 1e+200 + 1j)
    a = 3.33 + 4.43j
    self.assertEqual(a ** 0j, 1)
    self.assertEqual(a ** 0.0 + 0j, 1)
    self.assertEqual(3j ** 0j, 1)
    self.assertEqual(3j ** 0, 1)
    try:
        0j ** a
    except ZeroDivisionError:
        pass
    else:
        self.fail('should fail 0.0 to negative or complex power')
    try:
        0j ** (3 - 2j)
    except ZeroDivisionError:
        pass
    else:
        self.fail('should fail 0.0 to negative or complex power')
    self.assertEqual(a ** 105, a ** 105)
    self.assertEqual(a ** (-105), a ** (-105))
    self.assertEqual(a ** (-30), a ** (-30))
    self.assertEqual(0j ** 0, 1)
    b = 5.1 + 2.3j
    self.assertRaises(ValueError, pow, a, b, 0)
    values = (sys.maxsize, sys.maxsize + 1, sys.maxsize - 1, -sys.maxsize, -sys.maxsize + 1, -sys.maxsize + 1)
    for real in values:
        for imag in values:
            with self.subTest(real=real, imag=imag):
                c = complex(real, imag)
                try:
                    c ** real
                except OverflowError:
                    pass
                try:
                    c ** c
                except OverflowError:
                    pass
