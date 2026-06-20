# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_cookies

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cj = MockCookieJar()
    h = urllib.request.HTTPCookieProcessor(cj)
    h.parent = MockOpener()
    req = Request('http://example.com/')
    r = MockResponse(200, 'OK', {}, '')
    newreq = h.http_request(req)
    self.assertIs(cj.ach_req, req)
    self.assertIs(cj.ach_req, newreq)
    self.assertEqual(req.origin_req_host, 'example.com')
    self.assertFalse(req.unverifiable)
    newr = h.http_response(req, r)
    self.assertIs(cj.ec_req, req)
    self.assertIs(cj.ec_r, r)
    self.assertIs(r, newr)
