# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, unicodedata.name)
    self.assertRaises(TypeError, unicodedata.name, 'xx')
    self.assertRaises(TypeError, unicodedata.lookup)
    self.assertRaises(KeyError, unicodedata.lookup, 'unknown')
