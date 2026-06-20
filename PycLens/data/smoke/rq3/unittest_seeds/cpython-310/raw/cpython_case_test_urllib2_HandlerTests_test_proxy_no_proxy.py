# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_proxy_no_proxy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.environ['no_proxy'] = 'python.org'
    o = OpenerDirector()
    ph = urllib.request.ProxyHandler(dict(http='proxy.example.com'))
    o.add_handler(ph)
    req = Request('http://www.perl.org/')
    self.assertEqual(req.host, 'www.perl.org')
    o.open(req)
    self.assertEqual(req.host, 'proxy.example.com')
    req = Request('http://www.python.org')
    self.assertEqual(req.host, 'www.python.org')
    o.open(req)
    self.assertEqual(req.host, 'www.python.org')
    del os.environ['no_proxy']
