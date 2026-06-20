# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: OpenerDirectorTests_test_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    meth_spec = [[('http_open', 'raise')], [('http_open', 'return self')]]
    handlers = add_ordered_mock_handlers(o, meth_spec)
    req = Request('http://example.com/')
    self.assertRaises(urllib.error.URLError, o.open, req)
    self.assertEqual(o.calls, [(handlers[0], 'http_open', (req,), {})])
