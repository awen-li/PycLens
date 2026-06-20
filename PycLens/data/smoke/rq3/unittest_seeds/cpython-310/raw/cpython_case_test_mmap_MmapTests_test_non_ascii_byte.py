# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_non_ascii_byte

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for b in (129, 200, 255):
        m = mmap.mmap(-1, 1)
        m.write_byte(b)
        self.assertEqual(m[0], b)
        m.seek(0)
        self.assertEqual(m.read_byte(), b)
        m.close()
