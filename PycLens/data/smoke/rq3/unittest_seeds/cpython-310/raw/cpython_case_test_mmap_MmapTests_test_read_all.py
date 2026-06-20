# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_read_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = mmap.mmap(-1, 16)
    self.addCleanup(m.close)
    m.write(bytes(range(16)))
    m.seek(0)
    self.assertEqual(m.read(), bytes(range(16)))
    m.seek(8)
    self.assertEqual(m.read(), bytes(range(8, 16)))
    m.seek(16)
    self.assertEqual(m.read(), b'')
    m.seek(3)
    self.assertEqual(m.read(None), bytes(range(3, 16)))
    m.seek(4)
    self.assertEqual(m.read(-1), bytes(range(4, 16)))
    m.seek(5)
    self.assertEqual(m.read(-2), bytes(range(5, 16)))
    m.seek(9)
    self.assertEqual(m.read(-42), bytes(range(9, 16)))
