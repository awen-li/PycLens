# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_constructor_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(), '')
    self.assertEqual(str(errors='strict'), '')
    utf8_cent = '¢'.encode('utf-8')
    self.assertEqual(str(utf8_cent, errors='strict'), '¢')
    self.assertRaises(UnicodeDecodeError, str, utf8_cent, encoding='ascii')
