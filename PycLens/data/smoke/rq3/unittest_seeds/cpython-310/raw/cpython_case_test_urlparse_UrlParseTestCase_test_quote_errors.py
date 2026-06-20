# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_quote_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, urllib.parse.quote, b'foo', encoding='utf-8')
    self.assertRaises(TypeError, urllib.parse.quote, b'foo', errors='strict')
