# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_portseparator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(urllib.parse.urlparse('http:80'), ('http', '', '80', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('https:80'), ('https', '', '80', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('path:80'), ('path', '', '80', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('http:'), ('http', '', '', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('https:'), ('https', '', '', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('http://www.python.org:80'), ('http', 'www.python.org:80', '', '', '', ''))
    self.assertEqual(urllib.parse.urlparse(b'http:80'), (b'http', b'', b'80', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'https:80'), (b'https', b'', b'80', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'path:80'), (b'path', b'', b'80', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'http:'), (b'http', b'', b'', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'https:'), (b'https', b'', b'', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'http://www.python.org:80'), (b'http', b'www.python.org:80', b'', b'', b'', b''))
