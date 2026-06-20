# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: OpenerDirectorTests_test_handler_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    handlers = []
    for (meths, handler_order) in [([('http_open', 'return self')], 500), (['http_open'], 0)]:

        class MockHandlerSubclass(MockHandler):
            pass
        h = MockHandlerSubclass(meths)
        h.handler_order = handler_order
        handlers.append(h)
        o.add_handler(h)
    o.open('http://example.com/')
    self.assertEqual(o.calls[0][0], handlers[1])
    self.assertEqual(o.calls[1][0], handlers[0])
