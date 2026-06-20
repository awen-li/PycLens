# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: BinaryTestCase_test_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = b'\x01\x02\x03abc123\xff\xfe'
    t = xmlrpclib.Binary(d)
    self.assertEqual(str(t), str(d, 'latin-1'))
