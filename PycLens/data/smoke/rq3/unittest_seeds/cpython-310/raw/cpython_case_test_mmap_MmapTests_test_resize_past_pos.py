# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_resize_past_pos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = mmap.mmap(-1, 8192)
    self.addCleanup(m.close)
    m.read(5000)
    try:
        m.resize(4096)
    except SystemError:
        self.skipTest('resizing not supported')
    self.assertEqual(m.read(14), b'')
    self.assertRaises(ValueError, m.read_byte)
    self.assertRaises(ValueError, m.write_byte, 42)
    self.assertRaises(ValueError, m.write, b'abc')
