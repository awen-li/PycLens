# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_missing_final_slash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = 'http://www.acme.com'
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    interact_2965(c, url, 'foo=bar; Version=1')
    req = urllib.request.Request(url)
    self.assertEqual(len(c), 1)
    c.add_cookie_header(req)
    self.assertTrue(req.has_header('Cookie'))
