# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_allow_dotted_names_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = xmlrpclib.ServerProxy('http://%s:%d/RPC2' % (ADDR, PORT))
    data = server.Fixture.getData()
    self.assertEqual(data, '42')
