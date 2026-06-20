# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_anyscheme

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(urllib.parse.urlparse('s3://foo.com/stuff'), ('s3', 'foo.com', '/stuff', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('x-newscheme://foo.com/stuff'), ('x-newscheme', 'foo.com', '/stuff', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('x-newscheme://foo.com/stuff?query#fragment'), ('x-newscheme', 'foo.com', '/stuff', '', 'query', 'fragment'))
    self.assertEqual(urllib.parse.urlparse('x-newscheme://foo.com/stuff?query'), ('x-newscheme', 'foo.com', '/stuff', '', 'query', ''))
    self.assertEqual(urllib.parse.urlparse(b's3://foo.com/stuff'), (b's3', b'foo.com', b'/stuff', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'x-newscheme://foo.com/stuff'), (b'x-newscheme', b'foo.com', b'/stuff', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'x-newscheme://foo.com/stuff?query#fragment'), (b'x-newscheme', b'foo.com', b'/stuff', b'', b'query', b'fragment'))
    self.assertEqual(urllib.parse.urlparse(b'x-newscheme://foo.com/stuff?query'), (b'x-newscheme', b'foo.com', b'/stuff', b'', b'query', b''))
