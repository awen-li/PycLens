# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_dump_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sample = b'my dog has fleas'
    self.assertEqual(sample, xmlrpclib.Binary(sample))
    for type_ in (bytes, bytearray, xmlrpclib.Binary):
        value = type_(sample)
        s = xmlrpclib.dumps((value,))
        (result, m) = xmlrpclib.loads(s, use_builtin_types=True)
        (newvalue,) = result
        self.assertEqual(newvalue, sample)
        self.assertIs(type(newvalue), bytes)
        self.assertIsNone(m)
        (result, m) = xmlrpclib.loads(s, use_builtin_types=False)
        (newvalue,) = result
        self.assertEqual(newvalue, sample)
        self.assertIs(type(newvalue), xmlrpclib.Binary)
        self.assertIsNone(m)
