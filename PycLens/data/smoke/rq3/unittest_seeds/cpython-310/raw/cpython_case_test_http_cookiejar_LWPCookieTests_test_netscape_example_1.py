# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_netscape_example_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    year_plus_one = time.localtime()[0] + 1
    headers = []
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    req = urllib.request.Request('http://www.acme.com:80/', headers={'Host': 'www.acme.com:80'})
    headers.append('Set-Cookie: CUSTOMER=WILE_E_COYOTE; path=/ ; expires=Wednesday, 09-Nov-%d 23:12:40 GMT' % year_plus_one)
    res = FakeResponse(headers, 'http://www.acme.com/')
    c.extract_cookies(res, req)
    req = urllib.request.Request('http://www.acme.com/')
    c.add_cookie_header(req)
    self.assertEqual(req.get_header('Cookie'), 'CUSTOMER=WILE_E_COYOTE')
    self.assertEqual(req.get_header('Cookie2'), '$Version="1"')
    headers.append('Set-Cookie: PART_NUMBER=ROCKET_LAUNCHER_0001; path=/')
    res = FakeResponse(headers, 'http://www.acme.com/')
    c.extract_cookies(res, req)
    req = urllib.request.Request('http://www.acme.com/foo/bar')
    c.add_cookie_header(req)
    h = req.get_header('Cookie')
    self.assertIn('PART_NUMBER=ROCKET_LAUNCHER_0001', h)
    self.assertIn('CUSTOMER=WILE_E_COYOTE', h)
    headers.append('Set-Cookie: SHIPPING=FEDEX; path=/foo')
    res = FakeResponse(headers, 'http://www.acme.com')
    c.extract_cookies(res, req)
    req = urllib.request.Request('http://www.acme.com/')
    c.add_cookie_header(req)
    h = req.get_header('Cookie')
    self.assertIn('PART_NUMBER=ROCKET_LAUNCHER_0001', h)
    self.assertIn('CUSTOMER=WILE_E_COYOTE', h)
    self.assertNotIn('SHIPPING=FEDEX', h)
    req = urllib.request.Request('http://www.acme.com/foo/')
    c.add_cookie_header(req)
    h = req.get_header('Cookie')
    self.assertIn('PART_NUMBER=ROCKET_LAUNCHER_0001', h)
    self.assertIn('CUSTOMER=WILE_E_COYOTE', h)
    self.assertTrue(h.startswith('SHIPPING=FEDEX;'))
