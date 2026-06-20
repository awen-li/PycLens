# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_intranet_domains_ns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(DefaultCookiePolicy(rfc2965=False))
    interact_netscape(c, 'http://example/', 'foo1=bar')
    cookie = interact_netscape(c, 'http://example/', 'foo2=bar; domain=.local')
    self.assertEqual(len(c), 2)
    self.assertIn('foo1=bar', cookie)
    cookie = interact_netscape(c, 'http://example/')
    self.assertIn('foo2=bar', cookie)
    self.assertEqual(len(c), 2)
