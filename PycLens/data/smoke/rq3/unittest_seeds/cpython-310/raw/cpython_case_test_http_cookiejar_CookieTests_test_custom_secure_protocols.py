# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_custom_secure_protocols

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy(secure_protocols=['foos'])
    c = CookieJar(policy=pol)
    headers = ['Set-Cookie: session=narf; secure; path=/']
    req = urllib.request.Request('https://www.acme.com/')
    res = FakeResponse(headers, 'https://www.acme.com/')
    c.extract_cookies(res, req)
    self.assertEqual(len(c), 1)
    req = urllib.request.Request('https://www.acme.com/')
    c.add_cookie_header(req)
    self.assertFalse(req.has_header('Cookie'))
    req = urllib.request.Request('http://www.acme.com/')
    c.add_cookie_header(req)
    self.assertFalse(req.has_header('Cookie'))
    req = urllib.request.Request('foos://www.acme.com/')
    c.add_cookie_header(req)
    self.assertTrue(req.has_header('Cookie'))
    req = urllib.request.Request('foo://www.acme.com/')
    c.add_cookie_header(req)
    self.assertFalse(req.has_header('Cookie'))
