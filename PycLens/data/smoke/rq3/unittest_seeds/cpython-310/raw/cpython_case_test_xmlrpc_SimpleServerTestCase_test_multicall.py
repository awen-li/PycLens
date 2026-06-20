# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_multicall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        p = xmlrpclib.ServerProxy(URL)
        multicall = xmlrpclib.MultiCall(p)
        multicall.add(2, 3)
        multicall.pow(6, 8)
        multicall.div(127, 42)
        (add_result, pow_result, div_result) = multicall()
        self.assertEqual(add_result, 2 + 3)
        self.assertEqual(pow_result, 6 ** 8)
        self.assertEqual(div_result, 127 // 42)
    except (xmlrpclib.ProtocolError, OSError) as e:
        if not is_unavailable_exception(e):
            self.fail('%s\n%s' % (e, getattr(e, 'headers', '')))
