# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_anonymous

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = mmap.mmap(-1, PAGESIZE)
    for x in range(PAGESIZE):
        self.assertEqual(m[x], 0, "anonymously mmap'ed contents should be zero")
    for x in range(PAGESIZE):
        b = x & 255
        m[x] = b
        self.assertEqual(m[x], b)
