# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: FormatFunctionsTestCase_test_setformat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for t in ('double', 'float'):
        float.__setformat__(t, 'unknown')
        if self.save_formats[t] == 'IEEE, big-endian':
            self.assertRaises(ValueError, float.__setformat__, t, 'IEEE, little-endian')
        elif self.save_formats[t] == 'IEEE, little-endian':
            self.assertRaises(ValueError, float.__setformat__, t, 'IEEE, big-endian')
        else:
            self.assertRaises(ValueError, float.__setformat__, t, 'IEEE, big-endian')
            self.assertRaises(ValueError, float.__setformat__, t, 'IEEE, little-endian')
        self.assertRaises(ValueError, float.__setformat__, t, 'chicken')
    self.assertRaises(ValueError, float.__setformat__, 'chicken', 'unknown')
