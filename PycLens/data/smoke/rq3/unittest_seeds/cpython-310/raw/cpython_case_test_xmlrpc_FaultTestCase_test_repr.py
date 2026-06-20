# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: FaultTestCase_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = xmlrpclib.Fault(42, 'Test Fault')
    self.assertEqual(repr(f), "<Fault 42: 'Test Fault'>")
    self.assertEqual(repr(f), str(f))
