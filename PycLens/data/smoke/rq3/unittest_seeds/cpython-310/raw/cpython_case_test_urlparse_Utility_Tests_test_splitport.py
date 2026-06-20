# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splitport

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitport = urllib.parse._splitport
    self.assertEqual(splitport('parrot:88'), ('parrot', '88'))
    self.assertEqual(splitport('parrot'), ('parrot', None))
    self.assertEqual(splitport('parrot:'), ('parrot', None))
    self.assertEqual(splitport('127.0.0.1'), ('127.0.0.1', None))
    self.assertEqual(splitport('parrot:cheese'), ('parrot:cheese', None))
    self.assertEqual(splitport('[::1]:88'), ('[::1]', '88'))
    self.assertEqual(splitport('[::1]'), ('[::1]', None))
    self.assertEqual(splitport(':88'), ('', '88'))
