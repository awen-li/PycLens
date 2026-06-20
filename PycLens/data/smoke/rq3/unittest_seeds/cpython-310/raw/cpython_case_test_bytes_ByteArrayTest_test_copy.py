# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'abc')
    bb = b.copy()
    self.assertEqual(bb, b'abc')
    b = bytearray(b'')
    bb = b.copy()
    self.assertEqual(bb, b'')
    b = bytearray(b'abc')
    bb = b.copy()
    self.assertEqual(b, bb)
    self.assertIsNot(b, bb)
    bb.append(ord('d'))
    self.assertEqual(bb, b'abcd')
    self.assertEqual(b, b'abc')
