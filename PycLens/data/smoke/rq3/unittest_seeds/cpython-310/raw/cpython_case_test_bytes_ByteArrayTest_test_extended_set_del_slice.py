# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_extended_set_del_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    indices = (0, None, 1, 3, 19, 300, 1 << 333, sys.maxsize, -1, -2, -31, -300)
    for start in indices:
        for stop in indices:
            for step in indices[1:]:
                L = list(range(255))
                b = bytearray(L)
                data = L[start:stop:step]
                data.reverse()
                L[start:stop:step] = data
                b[start:stop:step] = data
                self.assertEqual(b, bytearray(L))
                del L[start:stop:step]
                del b[start:stop:step]
                self.assertEqual(b, bytearray(L))
