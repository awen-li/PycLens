# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_unicode_host

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = xmlrpclib.ServerProxy('http://%s:%d/RPC2' % (ADDR, PORT))
    self.assertEqual(server.add('a', 'é'), 'aé')
