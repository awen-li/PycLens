# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_default_scheme

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for func in (urllib.parse.urlparse, urllib.parse.urlsplit):
        with self.subTest(function=func):
            result = func('http://example.net/', 'ftp')
            self.assertEqual(result.scheme, 'http')
            result = func(b'http://example.net/', b'ftp')
            self.assertEqual(result.scheme, b'http')
            self.assertEqual(func('path', 'ftp').scheme, 'ftp')
            self.assertEqual(func('path', scheme='ftp').scheme, 'ftp')
            self.assertEqual(func(b'path', scheme=b'ftp').scheme, b'ftp')
            self.assertEqual(func('path').scheme, '')
            self.assertEqual(func(b'path').scheme, b'')
            self.assertEqual(func(b'path', '').scheme, b'')
