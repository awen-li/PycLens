# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: FormatFunctionsTestCase_test_getformat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn(float.__getformat__('double'), ['unknown', 'IEEE, big-endian', 'IEEE, little-endian'])
    self.assertIn(float.__getformat__('float'), ['unknown', 'IEEE, big-endian', 'IEEE, little-endian'])
    self.assertRaises(ValueError, float.__getformat__, 'chicken')
    self.assertRaises(TypeError, float.__getformat__, 1)
