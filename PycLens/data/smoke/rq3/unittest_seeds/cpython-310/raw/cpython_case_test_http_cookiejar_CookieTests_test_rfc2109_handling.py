# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_rfc2109_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (rfc2109_as_netscape, rfc2965, version) in [(None, False, 0), (None, True, 1), (False, False, None), (False, True, 1), (True, False, 0), (True, True, 0)]:
        policy = DefaultCookiePolicy(rfc2109_as_netscape=rfc2109_as_netscape, rfc2965=rfc2965)
        c = CookieJar(policy)
        interact_netscape(c, 'http://www.example.com/', 'ni=ni; Version=1')
        try:
            cookie = c._cookies['www.example.com']['/']['ni']
        except KeyError:
            self.assertIsNone(version)
        else:
            self.assertEqual(cookie.version, version)
            interact_2965(c, 'http://www.example.com/', 'foo=bar; Version=1')
            if rfc2965:
                cookie2965 = c._cookies['www.example.com']['/']['foo']
                self.assertEqual(cookie2965.version, 1)
