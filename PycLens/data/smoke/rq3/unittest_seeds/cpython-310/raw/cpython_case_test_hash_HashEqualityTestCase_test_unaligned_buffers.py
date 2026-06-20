# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashEqualityTestCase_test_unaligned_buffers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'123456789abcdefghijklmnopqrstuvwxyz' * 128
    for i in range(16):
        for j in range(16):
            aligned = b[i:128 + j]
            unaligned = memoryview(b)[i:128 + j]
            self.assertEqual(hash(aligned), hash(unaligned))
