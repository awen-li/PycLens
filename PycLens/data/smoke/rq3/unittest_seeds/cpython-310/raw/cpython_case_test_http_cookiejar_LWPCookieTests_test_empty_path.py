# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_empty_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    headers = []
    req = urllib.request.Request('http://www.ants.com/')
    headers.append('Set-Cookie: JSESSIONID=ABCDERANDOM123; Path=')
    res = FakeResponse(headers, 'http://www.ants.com/')
    c.extract_cookies(res, req)
    req = urllib.request.Request('http://www.ants.com/')
    c.add_cookie_header(req)
    self.assertEqual(req.get_header('Cookie'), 'JSESSIONID=ABCDERANDOM123')
    self.assertEqual(req.get_header('Cookie2'), '$Version="1"')
    req = urllib.request.Request('http://www.ants.com:8080')
    c.add_cookie_header(req)
    self.assertEqual(req.get_header('Cookie'), 'JSESSIONID=ABCDERANDOM123')
    self.assertEqual(req.get_header('Cookie2'), '$Version="1"')
