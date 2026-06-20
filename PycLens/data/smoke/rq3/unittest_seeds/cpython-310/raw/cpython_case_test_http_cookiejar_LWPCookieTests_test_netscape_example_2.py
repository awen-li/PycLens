# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_netscape_example_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar()
    headers = []
    req = urllib.request.Request('http://www.acme.com/')
    headers.append('Set-Cookie: PART_NUMBER=ROCKET_LAUNCHER_0001; path=/')
    res = FakeResponse(headers, 'http://www.acme.com/')
    c.extract_cookies(res, req)
    req = urllib.request.Request('http://www.acme.com/')
    c.add_cookie_header(req)
    self.assertEqual(req.get_header('Cookie'), 'PART_NUMBER=ROCKET_LAUNCHER_0001')
    headers.append('Set-Cookie: PART_NUMBER=RIDING_ROCKET_0023; path=/ammo')
    res = FakeResponse(headers, 'http://www.acme.com/')
    c.extract_cookies(res, req)
    req = urllib.request.Request('http://www.acme.com/ammo')
    c.add_cookie_header(req)
    self.assertRegex(req.get_header('Cookie'), 'PART_NUMBER=RIDING_ROCKET_0023;\\s*PART_NUMBER=ROCKET_LAUNCHER_0001')
