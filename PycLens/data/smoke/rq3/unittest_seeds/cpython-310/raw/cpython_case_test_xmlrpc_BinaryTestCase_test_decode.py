# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: BinaryTestCase_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = b'\x01\x02\x03abc123\xff\xfe'
    de = base64.encodebytes(d)
    t1 = xmlrpclib.Binary()
    t1.decode(de)
    self.assertEqual(str(t1), str(d, 'latin-1'))
    t2 = xmlrpclib._binary(de)
    self.assertEqual(str(t2), str(d, 'latin-1'))
