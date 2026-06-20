# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_to_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = urllib.parse._to_bytes('http://www.python.org')
    self.assertEqual(result, 'http://www.python.org')
    self.assertRaises(UnicodeError, urllib.parse._to_bytes, 'http://www.python.org/mediæval')
