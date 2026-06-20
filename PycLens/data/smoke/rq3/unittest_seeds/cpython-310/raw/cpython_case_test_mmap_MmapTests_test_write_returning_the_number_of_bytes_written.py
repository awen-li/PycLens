# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_write_returning_the_number_of_bytes_written

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mm = mmap.mmap(-1, 16)
    self.assertEqual(mm.write(b''), 0)
    self.assertEqual(mm.write(b'x'), 1)
    self.assertEqual(mm.write(b'yz'), 2)
    self.assertEqual(mm.write(b'python'), 6)
