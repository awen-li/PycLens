# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: InfNanTest_test_nan_from_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(isnan(float('nan')))
    self.assertTrue(isnan(float('+nan')))
    self.assertTrue(isnan(float('-nan')))
    self.assertEqual(repr(float('nan')), 'nan')
    self.assertEqual(repr(float('+nan')), 'nan')
    self.assertEqual(repr(float('-nan')), 'nan')
    self.assertEqual(repr(float('NAN')), 'nan')
    self.assertEqual(repr(float('+NAn')), 'nan')
    self.assertEqual(repr(float('-NaN')), 'nan')
    self.assertEqual(str(float('nan')), 'nan')
    self.assertEqual(str(float('+nan')), 'nan')
    self.assertEqual(str(float('-nan')), 'nan')
    self.assertRaises(ValueError, float, 'nana')
    self.assertRaises(ValueError, float, '+nana')
    self.assertRaises(ValueError, float, '-nana')
    self.assertRaises(ValueError, float, 'na')
    self.assertRaises(ValueError, float, '+na')
    self.assertRaises(ValueError, float, '-na')
    self.assertRaises(ValueError, float, '++nan')
    self.assertRaises(ValueError, float, '-+NAN')
    self.assertRaises(ValueError, float, '+-NaN')
    self.assertRaises(ValueError, float, '--nAn')
