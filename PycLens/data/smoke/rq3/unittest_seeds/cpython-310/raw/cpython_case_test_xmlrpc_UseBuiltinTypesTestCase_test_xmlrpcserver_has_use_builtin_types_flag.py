# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: UseBuiltinTypesTestCase_test_xmlrpcserver_has_use_builtin_types_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 0), use_builtin_types=True)
    server.server_close()
    self.assertTrue(server.use_builtin_types)
