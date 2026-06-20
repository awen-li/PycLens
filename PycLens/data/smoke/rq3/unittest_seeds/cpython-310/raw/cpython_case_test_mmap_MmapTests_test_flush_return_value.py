# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_flush_return_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mm = mmap.mmap(-1, 16)
    self.addCleanup(mm.close)
    mm.write(b'python')
    result = mm.flush()
    self.assertIsNone(result)
    if sys.platform.startswith('linux'):
        self.assertRaises(OSError, mm.flush, 1, len(b'python'))
