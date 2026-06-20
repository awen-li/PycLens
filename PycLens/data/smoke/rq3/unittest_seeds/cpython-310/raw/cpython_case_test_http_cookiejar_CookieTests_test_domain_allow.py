# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_domain_allow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(policy=DefaultCookiePolicy(blocked_domains=['acme.com'], allowed_domains=['www.acme.com']))
    req = urllib.request.Request('http://acme.com/')
    headers = ['Set-Cookie: CUSTOMER=WILE_E_COYOTE; path=/']
    res = FakeResponse(headers, 'http://acme.com/')
    c.extract_cookies(res, req)
    self.assertEqual(len(c), 0)
    req = urllib.request.Request('http://www.acme.com/')
    res = FakeResponse(headers, 'http://www.acme.com/')
    c.extract_cookies(res, req)
    self.assertEqual(len(c), 1)
    req = urllib.request.Request('http://www.coyote.com/')
    res = FakeResponse(headers, 'http://www.coyote.com/')
    c.extract_cookies(res, req)
    self.assertEqual(len(c), 1)
    req = urllib.request.Request('http://www.coyote.com/')
    res = FakeResponse(headers, 'http://www.coyote.com/')
    cookies = c.make_cookies(res, req)
    c.set_cookie(cookies[0])
    self.assertEqual(len(c), 2)
    c.add_cookie_header(req)
    self.assertFalse(req.has_header('Cookie'))
