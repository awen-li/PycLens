# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_non_existing_multicall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        p = xmlrpclib.ServerProxy(URL)
        multicall = xmlrpclib.MultiCall(p)
        multicall.this_is_not_exists()
        result = multicall()
        self.assertEqual(result.results[0]['faultCode'], 1)
        self.assertEqual(result.results[0]['faultString'], '<class \'Exception\'>:method "this_is_not_exists" is not supported')
    except (xmlrpclib.ProtocolError, OSError) as e:
        if not is_unavailable_exception(e):
            self.fail('%s\n%s' % (e, getattr(e, 'headers', '')))
