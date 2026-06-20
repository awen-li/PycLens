# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_b2a_base64_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'hello')
    self.assertEqual(binascii.b2a_base64(b), b'aGVsbG8=\n')
    self.assertEqual(binascii.b2a_base64(b, newline=True), b'aGVsbG8=\n')
    self.assertEqual(binascii.b2a_base64(b, newline=False), b'aGVsbG8=')
