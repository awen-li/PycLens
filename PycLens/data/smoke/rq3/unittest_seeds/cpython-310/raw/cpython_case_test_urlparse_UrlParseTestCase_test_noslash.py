# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_noslash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(urllib.parse.urlparse('http://example.com?blahblah=/foo'), ('http', 'example.com', '', '', 'blahblah=/foo', ''))
    self.assertEqual(urllib.parse.urlparse(b'http://example.com?blahblah=/foo'), (b'http', b'example.com', b'', b'', b'blahblah=/foo', b''))
