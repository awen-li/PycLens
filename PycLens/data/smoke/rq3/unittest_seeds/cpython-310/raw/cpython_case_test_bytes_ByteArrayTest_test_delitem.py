# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(range(10))
    del b[0]
    self.assertEqual(b, bytearray(range(1, 10)))
    del b[-1]
    self.assertEqual(b, bytearray(range(1, 9)))
    del b[4]
    self.assertEqual(b, bytearray([1, 2, 3, 4, 6, 7, 8]))
