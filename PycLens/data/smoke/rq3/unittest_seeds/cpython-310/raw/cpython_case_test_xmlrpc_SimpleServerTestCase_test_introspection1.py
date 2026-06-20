# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_introspection1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_methods = set(['pow', 'div', 'my_function', 'add', 'têšt', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'Fixture'])
    try:
        p = xmlrpclib.ServerProxy(URL)
        meth = p.system.listMethods()
        self.assertEqual(set(meth), expected_methods)
    except (xmlrpclib.ProtocolError, OSError) as e:
        if not is_unavailable_exception(e):
            self.fail('%s\n%s' % (e, getattr(e, 'headers', '')))
