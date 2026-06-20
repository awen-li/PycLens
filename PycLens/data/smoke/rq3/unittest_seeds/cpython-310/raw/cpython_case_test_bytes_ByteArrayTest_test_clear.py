# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'python')
    b.clear()
    self.assertEqual(b, b'')
    b = bytearray(b'')
    b.clear()
    self.assertEqual(b, b'')
    b = bytearray(b'')
    b.append(ord('r'))
    b.clear()
    b.append(ord('p'))
    self.assertEqual(b, b'p')
