# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splittag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splittag = urllib.parse._splittag
    self.assertEqual(splittag('http://example.com?foo=bar#baz'), ('http://example.com?foo=bar', 'baz'))
    self.assertEqual(splittag('http://example.com?foo=bar#'), ('http://example.com?foo=bar', ''))
    self.assertEqual(splittag('#baz'), ('', 'baz'))
    self.assertEqual(splittag('http://example.com?foo=bar'), ('http://example.com?foo=bar', None))
    self.assertEqual(splittag('http://example.com?foo=bar#baz#boo'), ('http://example.com?foo=bar#baz', 'boo'))
