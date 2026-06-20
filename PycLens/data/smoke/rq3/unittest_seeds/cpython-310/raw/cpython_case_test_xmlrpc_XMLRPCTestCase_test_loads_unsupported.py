# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_loads_unsupported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ResponseError = xmlrpclib.ResponseError
    data = '<params><param><value><spam/></value></param></params>'
    self.assertRaises(ResponseError, xmlrpclib.loads, data)
    data = '<params><param><value><array><value><spam/></value></array></value></param></params>'
    self.assertRaises(ResponseError, xmlrpclib.loads, data)
    data = '<params><param><value><struct><member><name>a</name><value><spam/></value></member><member><name>b</name><value><spam/></value></member></struct></value></param></params>'
    self.assertRaises(ResponseError, xmlrpclib.loads, data)
