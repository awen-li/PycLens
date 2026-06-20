# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'world')
    self.assertEqual(b.pop(), ord('d'))
    self.assertEqual(b.pop(0), ord('w'))
    self.assertEqual(b.pop(-2), ord('r'))
    self.assertRaises(IndexError, lambda : b.pop(10))
    self.assertRaises(IndexError, lambda : bytearray().pop())
    self.assertEqual(bytearray(b'\xff').pop(), 255)
