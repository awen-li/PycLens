# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with xmlrpclib.ServerProxy(URL) as server:
        server.add(2, 3)
        self.assertNotEqual(server('transport')._connection, (None, None))
    self.assertEqual(server('transport')._connection, (None, None))
