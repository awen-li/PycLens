# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_length_0_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as f:
        f.write(65536 * 2 * b'm')
    with open(TESTFN, 'rb') as f:
        with mmap.mmap(f.fileno(), 0, offset=65536, access=mmap.ACCESS_READ) as mf:
            self.assertRaises(IndexError, mf.__getitem__, 80000)
