# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: FormatTestCase_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(format(0.0, 'f'), '0.000000')
    self.assertEqual(format(0.0, ''), '0.0')
    self.assertEqual(format(0.01, ''), '0.01')
    self.assertEqual(format(0.01, 'g'), '0.01')
    x = 100 / 7.0
    self.assertEqual(format(x, ''), str(x))
    self.assertEqual(format(x, '-'), str(x))
    self.assertEqual(format(x, '>'), str(x))
    self.assertEqual(format(x, '2'), str(x))
    self.assertEqual(format(1.0, 'f'), '1.000000')
    self.assertEqual(format(-1.0, 'f'), '-1.000000')
    self.assertEqual(format(1.0, ' f'), ' 1.000000')
    self.assertEqual(format(-1.0, ' f'), '-1.000000')
    self.assertEqual(format(1.0, '+f'), '+1.000000')
    self.assertEqual(format(-1.0, '+f'), '-1.000000')
    self.assertEqual(format(-1.0, '%'), '-100.000000%')
    self.assertRaises(ValueError, format, 3.0, 's')
    for format_spec in [chr(x) for x in range(ord('a'), ord('z') + 1)] + [chr(x) for x in range(ord('A'), ord('Z') + 1)]:
        if not format_spec in 'eEfFgGn%':
            self.assertRaises(ValueError, format, 0.0, format_spec)
            self.assertRaises(ValueError, format, 1.0, format_spec)
            self.assertRaises(ValueError, format, -1.0, format_spec)
            self.assertRaises(ValueError, format, 1e+100, format_spec)
            self.assertRaises(ValueError, format, -1e+100, format_spec)
            self.assertRaises(ValueError, format, 1e-100, format_spec)
            self.assertRaises(ValueError, format, -1e-100, format_spec)
    self.assertEqual(format(NAN, 'f'), 'nan')
    self.assertEqual(format(NAN, 'F'), 'NAN')
    self.assertEqual(format(INF, 'f'), 'inf')
    self.assertEqual(format(INF, 'F'), 'INF')
