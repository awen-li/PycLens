# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_cookie_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from http.cookiejar import CookieJar
    from test.test_http_cookiejar import interact_netscape
    cj = CookieJar()
    interact_netscape(cj, 'http://www.example.com/', 'spam=eggs')
    hh = MockHTTPHandler(302, 'Location: http://www.cracker.com/\r\n\r\n')
    hdeh = urllib.request.HTTPDefaultErrorHandler()
    hrh = urllib.request.HTTPRedirectHandler()
    cp = urllib.request.HTTPCookieProcessor(cj)
    o = build_test_opener(hh, hdeh, hrh, cp)
    o.open('http://www.example.com/')
    self.assertFalse(hh.req.has_header('Cookie'))
