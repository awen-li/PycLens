# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_extended_set_del_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = bytes(reversed(range(256)))
    m = mmap.mmap(-1, len(s))
    indices = (0, None, 1, 3, 19, 300, sys.maxsize, -1, -2, -31, -300)
    for start in indices:
        for stop in indices:
            for step in indices[1:]:
                m[:] = s
                self.assertEqual(m[:], s)
                L = list(s)
                data = L[start:stop:step]
                data = bytes(reversed(data))
                L[start:stop:step] = data
                m[start:stop:step] = data
                self.assertEqual(m[:], bytes(L))
