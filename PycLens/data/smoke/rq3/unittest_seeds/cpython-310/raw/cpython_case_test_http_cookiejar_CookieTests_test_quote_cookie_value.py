# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_quote_cookie_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(policy=DefaultCookiePolicy(rfc2965=True))
    interact_2965(c, 'http://www.acme.com/', 'foo=\\b"a"r; Version=1')
    h = interact_2965(c, 'http://www.acme.com/')
    self.assertEqual(h, '$Version=1; foo=\\\\b\\"a\\"r')
