# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_float_with_comma

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import locale
    if not locale.localeconv()['decimal_point'] == ',':
        self.skipTest('decimal_point is not ","')
    self.assertEqual(float('  3.14  '), 3.14)
    self.assertEqual(float('+3.14  '), 3.14)
    self.assertEqual(float('-3.14  '), -3.14)
    self.assertEqual(float('.14  '), 0.14)
    self.assertEqual(float('3.  '), 3.0)
    self.assertEqual(float('3.e3  '), 3000.0)
    self.assertEqual(float('3.2e3  '), 3200.0)
    self.assertEqual(float('2.5e-1  '), 0.25)
    self.assertEqual(float('5e-1'), 0.5)
    self.assertRaises(ValueError, float, '  3,14  ')
    self.assertRaises(ValueError, float, '  +3,14  ')
    self.assertRaises(ValueError, float, '  -3,14  ')
    self.assertRaises(ValueError, float, '  0x3.1  ')
    self.assertRaises(ValueError, float, '  -0x3.p-1  ')
    self.assertRaises(ValueError, float, '  +0x3.p-1  ')
    self.assertEqual(float('  25.e-1  '), 2.5)
    self.assertAlmostEqual(float('  .25e-1  '), 0.025)
