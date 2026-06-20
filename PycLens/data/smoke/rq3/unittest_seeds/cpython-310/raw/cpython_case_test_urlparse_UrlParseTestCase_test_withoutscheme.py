# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_withoutscheme

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(urllib.parse.urlparse('path'), ('', '', 'path', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('//www.python.org:80'), ('', 'www.python.org:80', '', '', '', ''))
    self.assertEqual(urllib.parse.urlparse('http://www.python.org:80'), ('http', 'www.python.org:80', '', '', '', ''))
    self.assertEqual(urllib.parse.urlparse(b'path'), (b'', b'', b'path', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'//www.python.org:80'), (b'', b'www.python.org:80', b'', b'', b'', b''))
    self.assertEqual(urllib.parse.urlparse(b'http://www.python.org:80'), (b'http', b'www.python.org:80', b'', b'', b'', b''))
