# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_netscape_misc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar()
    headers = []
    req = urllib.request.Request('http://foo.bar.acme.com/foo')
    headers.append('Set-Cookie: Customer=WILE_E_COYOTE; domain=.acme.com')
    res = FakeResponse(headers, 'http://www.acme.com/foo')
    c.extract_cookies(res, req)
    headers.append('Set-Cookie: PART_NUMBER=3,4; domain=foo.bar.acme.com')
    res = FakeResponse(headers, 'http://www.acme.com/foo')
    c.extract_cookies(res, req)
    req = urllib.request.Request('http://foo.bar.acme.com/foo')
    c.add_cookie_header(req)
    self.assertIn('PART_NUMBER=3,4', req.get_header('Cookie'))
    self.assertIn('Customer=WILE_E_COYOTE', req.get_header('Cookie'))
