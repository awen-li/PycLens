# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: FaultTestCase_test_dump_fault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = xmlrpclib.Fault(42, 'Test Fault')
    s = xmlrpclib.dumps((f,))
    ((newf,), m) = xmlrpclib.loads(s)
    self.assertEqual(newf, {'faultCode': 42, 'faultString': 'Test Fault'})
    self.assertEqual(m, None)
    s = xmlrpclib.Marshaller().dumps(f)
    self.assertRaises(xmlrpclib.Fault, xmlrpclib.loads, s)
