# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_bug_1164912

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = xmlrpclib.DateTime()
    ((new_d,), dummy) = xmlrpclib.loads(xmlrpclib.dumps((d,), methodresponse=True))
    self.assertIsInstance(new_d.value, str)
    s = xmlrpclib.dumps((new_d,), methodresponse=True)
    self.assertIsInstance(s, str)
