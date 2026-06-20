# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_read_invalid_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = mmap.mmap(-1, 16)
    self.addCleanup(m.close)
    self.assertRaises(TypeError, m.read, 'foo')
    self.assertRaises(TypeError, m.read, 5.5)
    self.assertRaises(TypeError, m.read, [1, 2, 3])
