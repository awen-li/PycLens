# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_secure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for ns in (True, False):
        for whitespace in (' ', ''):
            c = CookieJar()
            if ns:
                pol = DefaultCookiePolicy(rfc2965=False)
                int = interact_netscape
                vs = ''
            else:
                pol = DefaultCookiePolicy(rfc2965=True)
                int = interact_2965
                vs = '; Version=1'
            c.set_policy(pol)
            url = 'http://www.acme.com/'
            int(c, url, 'foo1=bar%s%s' % (vs, whitespace))
            int(c, url, 'foo2=bar%s; secure%s' % (vs, whitespace))
            self.assertFalse(c._cookies['www.acme.com']['/']['foo1'].secure, 'non-secure cookie registered secure')
            self.assertTrue(c._cookies['www.acme.com']['/']['foo2'].secure, 'secure cookie registered non-secure')
