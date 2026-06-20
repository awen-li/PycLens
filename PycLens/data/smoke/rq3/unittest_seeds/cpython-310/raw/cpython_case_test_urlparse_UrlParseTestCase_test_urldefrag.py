# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_urldefrag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_cases = [('http://python.org#frag', 'http://python.org', 'frag'), ('http://python.org', 'http://python.org', ''), ('http://python.org/#frag', 'http://python.org/', 'frag'), ('http://python.org/', 'http://python.org/', ''), ('http://python.org/?q#frag', 'http://python.org/?q', 'frag'), ('http://python.org/?q', 'http://python.org/?q', ''), ('http://python.org/p#frag', 'http://python.org/p', 'frag'), ('http://python.org/p?q', 'http://python.org/p?q', ''), (RFC1808_BASE, 'http://a/b/c/d;p?q', 'f'), (RFC2396_BASE, 'http://a/b/c/d;p?q', '')]

    def _encode(t):
        return type(t)((x.encode('ascii') for x in t))
    bytes_cases = [_encode(x) for x in str_cases]
    for (url, defrag, frag) in str_cases + bytes_cases:
        result = urllib.parse.urldefrag(url)
        self.assertEqual(result.geturl(), url)
        self.assertEqual(result, (defrag, frag))
        self.assertEqual(result.url, defrag)
        self.assertEqual(result.fragment, frag)
