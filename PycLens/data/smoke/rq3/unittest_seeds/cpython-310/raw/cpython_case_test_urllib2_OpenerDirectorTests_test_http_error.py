# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: OpenerDirectorTests_test_http_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    meth_spec = [[('http_open', 'error 302')], [('http_error_400', 'raise'), 'http_open'], [('http_error_302', 'return response'), 'http_error_303', 'http_error'], ['http_error_302']]
    handlers = add_ordered_mock_handlers(o, meth_spec)
    req = Request('http://example.com/')
    o.open(req)
    assert len(o.calls) == 2
    calls = [(handlers[0], 'http_open', (req,)), (handlers[2], 'http_error_302', (req, support.ALWAYS_EQ, 302, '', {}))]
    for (expected, got) in zip(calls, o.calls):
        (handler, method_name, args) = expected
        self.assertEqual((handler, method_name), got[:2])
        self.assertEqual(args, got[2])
