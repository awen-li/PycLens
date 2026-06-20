# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_get_host_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    transp = xmlrpc.client.Transport()
    self.assertEqual(transp.get_host_info('user@host.tld'), ('host.tld', [('Authorization', 'Basic dXNlcg==')], {}))
