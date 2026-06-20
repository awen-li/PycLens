# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_proxy_https_proxy_authorization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    ph = urllib.request.ProxyHandler(dict(https='proxy.example.com:3128'))
    o.add_handler(ph)
    https_handler = MockHTTPSHandler()
    o.add_handler(https_handler)
    req = Request('https://www.example.com/')
    req.add_header('Proxy-Authorization', 'FooBar')
    req.add_header('User-Agent', 'Grail')
    self.assertEqual(req.host, 'www.example.com')
    self.assertIsNone(req._tunnel_host)
    o.open(req)
    self.assertNotIn(('Proxy-Authorization', 'FooBar'), https_handler.httpconn.req_headers)
    self.assertIn(('User-Agent', 'Grail'), https_handler.httpconn.req_headers)
    self.assertIsNotNone(req._tunnel_host)
    self.assertEqual(req.host, 'proxy.example.com:3128')
    self.assertEqual(req.get_header('Proxy-authorization'), 'FooBar')
