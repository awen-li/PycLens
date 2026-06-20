# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_setslice_extend

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(range(100))
    self.assertEqual(list(b), list(range(100)))
    del b[:10]
    self.assertEqual(list(b), list(range(10, 100)))
    b.extend(range(100, 110))
    self.assertEqual(list(b), list(range(10, 110)))
