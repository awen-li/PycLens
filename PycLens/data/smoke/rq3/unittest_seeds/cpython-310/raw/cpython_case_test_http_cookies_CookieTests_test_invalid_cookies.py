# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_invalid_cookies

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie()
    for s in (']foo=x', '[foo=x', 'blah]foo=x', 'blah[foo=x', 'Set-Cookie: foo=bar', 'Set-Cookie: foo', 'foo=bar; baz', 'baz; foo=bar', 'secure;foo=bar', 'Version=1;foo=bar'):
        C.load(s)
        self.assertEqual(dict(C), {})
        self.assertEqual(C.output(), '')
