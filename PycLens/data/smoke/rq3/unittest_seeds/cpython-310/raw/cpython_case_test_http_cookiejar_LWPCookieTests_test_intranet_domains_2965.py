# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_intranet_domains_2965

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    interact_2965(c, 'http://example/', 'foo1=bar; PORT; Discard; Version=1;')
    cookie = interact_2965(c, 'http://example/', 'foo2=bar; domain=".local"; Version=1')
    self.assertIn('foo1=bar', cookie)
    interact_2965(c, 'http://example/', 'foo3=bar; Version=1')
    cookie = interact_2965(c, 'http://example/')
    self.assertIn('foo2=bar', cookie)
    self.assertEqual(len(c), 3)
