# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_alloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray()
    alloc = b.__alloc__()
    self.assertGreaterEqual(alloc, 0)
    seq = [alloc]
    for i in range(100):
        b += b'x'
        alloc = b.__alloc__()
        self.assertGreater(alloc, len(b))
        if alloc not in seq:
            seq.append(alloc)
