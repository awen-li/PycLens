# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: OpenerDirectorTests_test_badly_named_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from urllib.error import URLError
    o = OpenerDirector()
    meth_spec = [[('do_open', 'return self'), ('proxy_open', 'return self')], [('redirect_request', 'return self')]]
    add_ordered_mock_handlers(o, meth_spec)
    o.add_handler(urllib.request.UnknownHandler())
    for scheme in ('do', 'proxy', 'redirect'):
        self.assertRaises(URLError, o.open, scheme + '://example.com/')
