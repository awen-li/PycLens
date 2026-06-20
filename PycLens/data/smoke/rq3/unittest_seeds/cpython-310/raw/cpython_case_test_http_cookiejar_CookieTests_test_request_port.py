# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_request_port

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    req = urllib.request.Request('http://www.acme.com:1234/', headers={'Host': 'www.acme.com:4321'})
    self.assertEqual(request_port(req), '1234')
    req = urllib.request.Request('http://www.acme.com/', headers={'Host': 'www.acme.com:4321'})
    self.assertEqual(request_port(req), DEFAULT_HTTP_PORT)
