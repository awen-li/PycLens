# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_unquote_to_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = urllib.parse.unquote_to_bytes('abc%20def')
    self.assertEqual(result, b'abc def')
    result = urllib.parse.unquote_to_bytes('')
    self.assertEqual(result, b'')
