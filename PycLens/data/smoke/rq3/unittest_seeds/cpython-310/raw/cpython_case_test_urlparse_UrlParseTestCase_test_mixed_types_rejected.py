# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_mixed_types_rejected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlparse('www.python.org', b'http')
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlparse(b'www.python.org', 'http')
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlsplit('www.python.org', b'http')
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlsplit(b'www.python.org', 'http')
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunparse((b'http', 'www.python.org', '', '', '', ''))
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunparse(('http', b'www.python.org', '', '', '', ''))
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunsplit((b'http', 'www.python.org', '', '', ''))
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunsplit(('http', b'www.python.org', '', '', ''))
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urljoin('http://python.org', b'http://python.org')
    with self.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urljoin(b'http://python.org', 'http://python.org')
