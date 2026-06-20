# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: OpenerDirectorTests_test_handled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    meth_spec = [['http_open', 'ftp_open', 'http_error_302'], ['ftp_open'], [('http_open', 'return self')], [('http_open', 'return self')]]
    handlers = add_ordered_mock_handlers(o, meth_spec)
    req = Request('http://example.com/')
    r = o.open(req)
    self.assertEqual(r, handlers[2])
    calls = [(handlers[0], 'http_open'), (handlers[2], 'http_open')]
    for (expected, got) in zip(calls, o.calls):
        (handler, name, args, kwds) = got
        self.assertEqual((handler, name), expected)
        self.assertEqual(args, (req,))
