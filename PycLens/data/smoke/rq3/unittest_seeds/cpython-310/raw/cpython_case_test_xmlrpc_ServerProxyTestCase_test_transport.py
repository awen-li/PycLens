# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: ServerProxyTestCase_test_transport

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = xmlrpclib.Transport()
    p = xmlrpclib.ServerProxy(self.url, transport=t)
    self.assertEqual(p('transport'), t)
