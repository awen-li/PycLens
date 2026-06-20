# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_http_roundtrips

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_cases = [('://www.python.org', ('www.python.org', '', '', '', ''), ('www.python.org', '', '', '')), ('://www.python.org#abc', ('www.python.org', '', '', '', 'abc'), ('www.python.org', '', '', 'abc')), ('://www.python.org?q=abc', ('www.python.org', '', '', 'q=abc', ''), ('www.python.org', '', 'q=abc', '')), ('://www.python.org/#abc', ('www.python.org', '/', '', '', 'abc'), ('www.python.org', '/', '', 'abc')), ('://a/b/c/d;p?q#f', ('a', '/b/c/d', 'p', 'q', 'f'), ('a', '/b/c/d;p', 'q', 'f'))]

    def _encode(t):
        return (t[0].encode('ascii'), tuple((x.encode('ascii') for x in t[1])), tuple((x.encode('ascii') for x in t[2])))
    bytes_cases = [_encode(x) for x in str_cases]
    str_schemes = ('http', 'https')
    bytes_schemes = (b'http', b'https')
    str_tests = (str_schemes, str_cases)
    bytes_tests = (bytes_schemes, bytes_cases)
    for (schemes, test_cases) in (str_tests, bytes_tests):
        for scheme in schemes:
            for (url, parsed, split) in test_cases:
                url = scheme + url
                parsed = (scheme,) + parsed
                split = (scheme,) + split
                self.checkRoundtrips(url, parsed, split)
