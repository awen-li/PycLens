# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_proxy_https

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    ph = urllib.request.ProxyHandler(dict(https='proxy.example.com:3128'))
    o.add_handler(ph)
    meth_spec = [[('https_open', 'return response')]]
    handlers = add_ordered_mock_handlers(o, meth_spec)
    req = Request('https://www.example.com/')
    self.assertEqual(req.host, 'www.example.com')
    o.open(req)
    self.assertEqual(req.host, 'proxy.example.com:3128')
    self.assertEqual([(handlers[0], 'https_open')], [tup[0:2] for tup in o.calls])
