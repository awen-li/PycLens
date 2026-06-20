# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splitquery

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitquery = urllib.parse._splitquery
    self.assertEqual(splitquery('http://python.org/fake?foo=bar'), ('http://python.org/fake', 'foo=bar'))
    self.assertEqual(splitquery('http://python.org/fake?foo=bar?'), ('http://python.org/fake?foo=bar', ''))
    self.assertEqual(splitquery('http://python.org/fake'), ('http://python.org/fake', None))
    self.assertEqual(splitquery('?foo=bar'), ('', 'foo=bar'))
