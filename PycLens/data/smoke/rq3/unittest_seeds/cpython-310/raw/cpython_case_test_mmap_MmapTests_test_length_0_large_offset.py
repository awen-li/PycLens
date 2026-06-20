# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_length_0_large_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb') as f:
        f.write(115699 * b'm')
    with open(TESTFN, 'w+b') as f:
        self.assertRaises(ValueError, mmap.mmap, f.fileno(), 0, offset=2147418112)
