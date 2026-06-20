# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_request_host

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    req = urllib.request.Request('http://1.1.1.1/', headers={'Host': 'www.acme.com:80'})
    self.assertEqual(request_host(req), '1.1.1.1')
    req = urllib.request.Request('http://www.acme.com/', headers={'Host': 'irrelevant.com'})
    self.assertEqual(request_host(req), 'www.acme.com')
    req = urllib.request.Request('http://www.acme.com:2345/resource.html', headers={'Host': 'www.acme.com:5432'})
    self.assertEqual(request_host(req), 'www.acme.com')
