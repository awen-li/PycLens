# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_repeat_after_setslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'abc')
    b[:2] = b'x'
    b1 = b * 1
    b3 = b * 3
    self.assertEqual(b1, b'xc')
    self.assertEqual(b1, b)
    self.assertEqual(b3, b'xcxcxc')
