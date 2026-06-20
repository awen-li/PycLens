# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_irepeat_1char

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'x')
    b1 = b
    b *= 100
    self.assertEqual(b, b'x' * 100)
    self.assertEqual(b, b1)
    self.assertIs(b, b1)
