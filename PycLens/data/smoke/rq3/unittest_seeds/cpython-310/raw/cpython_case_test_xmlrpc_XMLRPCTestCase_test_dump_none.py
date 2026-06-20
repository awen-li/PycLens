# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_dump_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value = alist + [None]
    arg1 = (alist + [None],)
    strg = xmlrpclib.dumps(arg1, allow_none=True)
    self.assertEqual(value, xmlrpclib.loads(strg)[0][0])
    self.assertRaises(TypeError, xmlrpclib.dumps, (arg1,))
