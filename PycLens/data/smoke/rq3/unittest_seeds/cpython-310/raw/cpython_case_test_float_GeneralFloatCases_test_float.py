# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(float(3.14), 3.14)
    self.assertEqual(float(314), 314.0)
    self.assertEqual(float('  3.14  '), 3.14)
    self.assertRaises(ValueError, float, '  0x3.1  ')
    self.assertRaises(ValueError, float, '  -0x3.p-1  ')
    self.assertRaises(ValueError, float, '  +0x3.p-1  ')
    self.assertRaises(ValueError, float, '++3.14')
    self.assertRaises(ValueError, float, '+-3.14')
    self.assertRaises(ValueError, float, '-+3.14')
    self.assertRaises(ValueError, float, '--3.14')
    self.assertRaises(ValueError, float, '.nan')
    self.assertRaises(ValueError, float, '+.inf')
    self.assertRaises(ValueError, float, '.')
    self.assertRaises(ValueError, float, '-.')
    self.assertRaises(TypeError, float, {})
    self.assertRaisesRegex(TypeError, "not 'dict'", float, {})
    self.assertRaises(ValueError, float, '\ud8f0')
    self.assertRaises(ValueError, float, '-1.7d29')
    self.assertRaises(ValueError, float, '3D-14')
    self.assertEqual(float('  ٣.١٤  '), 3.14)
    self.assertEqual(float('\u20033.14\u2002'), 3.14)
    float(b'.' + b'1' * 1000)
    float('.' + '1' * 1000)
    self.assertRaises(ValueError, float, 'こんにちは')
