# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splitnport

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitnport = urllib.parse._splitnport
    self.assertEqual(splitnport('parrot:88'), ('parrot', 88))
    self.assertEqual(splitnport('parrot'), ('parrot', -1))
    self.assertEqual(splitnport('parrot', 55), ('parrot', 55))
    self.assertEqual(splitnport('parrot:'), ('parrot', -1))
    self.assertEqual(splitnport('parrot:', 55), ('parrot', 55))
    self.assertEqual(splitnport('127.0.0.1'), ('127.0.0.1', -1))
    self.assertEqual(splitnport('127.0.0.1', 55), ('127.0.0.1', 55))
    self.assertEqual(splitnport('parrot:cheese'), ('parrot', None))
    self.assertEqual(splitnport('parrot:cheese', 55), ('parrot', None))
    self.assertEqual(splitnport('parrot: +1_0 '), ('parrot', None))
