# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: OpenerDirectorTests_test_processors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    meth_spec = [[('http_request', 'return request'), ('http_response', 'return response')], [('http_request', 'return request'), ('http_response', 'return response')]]
    handlers = add_ordered_mock_handlers(o, meth_spec)
    req = Request('http://example.com/')
    o.open(req)
    calls = [(handlers[0], 'http_request'), (handlers[1], 'http_request'), (handlers[0], 'http_response'), (handlers[1], 'http_response')]
    for (i, (handler, name, args, kwds)) in enumerate(o.calls):
        if i < 2:
            self.assertEqual((handler, name), calls[i])
            self.assertEqual(len(args), 1)
            self.assertIsInstance(args[0], Request)
        else:
            self.assertEqual((handler, name), calls[i])
            self.assertEqual(len(args), 2)
            self.assertIsInstance(args[0], Request)
            if args[1] is not None:
                self.assertIsInstance(args[1], MockResponse)
