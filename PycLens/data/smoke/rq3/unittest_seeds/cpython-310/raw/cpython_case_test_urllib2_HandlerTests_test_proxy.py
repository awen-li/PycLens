# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_proxy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = 'proxy.example.com:3128'
    for d in (dict(http=u), dict(HTTP=u)):
        o = OpenerDirector()
        ph = urllib.request.ProxyHandler(d)
        o.add_handler(ph)
        meth_spec = [[('http_open', 'return response')]]
        handlers = add_ordered_mock_handlers(o, meth_spec)
        req = Request('http://acme.example.com/')
        self.assertEqual(req.host, 'acme.example.com')
        o.open(req)
        self.assertEqual(req.host, u)
        self.assertEqual([(handlers[0], 'http_open')], [tup[0:2] for tup in o.calls])
