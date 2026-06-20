# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_urlencode_quote_via

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = urllib.parse.urlencode({'a': 'some value'})
    self.assertEqual(result, 'a=some+value')
    result = urllib.parse.urlencode({'a': 'some value/another'}, quote_via=urllib.parse.quote)
    self.assertEqual(result, 'a=some%20value%2Fanother')
    result = urllib.parse.urlencode({'a': 'some value/another'}, safe='/', quote_via=urllib.parse.quote)
    self.assertEqual(result, 'a=some%20value/another')
