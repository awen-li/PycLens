# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_bad_cookie_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cookiejar_from_cookie_headers(headers):
        c = CookieJar()
        req = urllib.request.Request('http://www.example.com/')
        r = FakeResponse(headers, 'http://www.example.com/')
        c.extract_cookies(r, req)
        return c
    future = time2netscape(time.time() + 3600)
    for headers in [['Set-Cookie: '], ['Set-Cookie2: '], ['Set-Cookie2: a=foo; path=/; Version=1; domain'], ['Set-Cookie: b=foo; max-age=oops'], ['Set-Cookie: b=foo; version=spam'], ['Set-Cookie:; Expires=%s' % future]]:
        c = cookiejar_from_cookie_headers(headers)
        self.assertEqual(len(c), 0)
    headers = ['Set-Cookie: c=foo; expires=Foo Bar 12 33:22:11 2000']
    c = cookiejar_from_cookie_headers(headers)
    cookie = c._cookies['www.example.com']['/']['c']
    self.assertIsNone(cookie.expires)
