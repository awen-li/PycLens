# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_madvise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = 2 * PAGESIZE
    m = mmap.mmap(-1, size)
    with self.assertRaisesRegex(ValueError, 'madvise start out of bounds'):
        m.madvise(mmap.MADV_NORMAL, size)
    with self.assertRaisesRegex(ValueError, 'madvise start out of bounds'):
        m.madvise(mmap.MADV_NORMAL, -1)
    with self.assertRaisesRegex(ValueError, 'madvise length invalid'):
        m.madvise(mmap.MADV_NORMAL, 0, -1)
    with self.assertRaisesRegex(OverflowError, 'madvise length too large'):
        m.madvise(mmap.MADV_NORMAL, PAGESIZE, sys.maxsize)
    self.assertEqual(m.madvise(mmap.MADV_NORMAL), None)
    self.assertEqual(m.madvise(mmap.MADV_NORMAL, PAGESIZE), None)
    self.assertEqual(m.madvise(mmap.MADV_NORMAL, PAGESIZE, size), None)
    self.assertEqual(m.madvise(mmap.MADV_NORMAL, 0, 2), None)
    self.assertEqual(m.madvise(mmap.MADV_NORMAL, 0, size), None)
