# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_rfind

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb+') as f:
        data = b'one two ones'
        n = len(data)
        f.write(data)
        f.flush()
        m = mmap.mmap(f.fileno(), n)
    self.assertEqual(m.rfind(b'one'), 8)
    self.assertEqual(m.rfind(b'one '), 0)
    self.assertEqual(m.rfind(b'one', 0, -1), 8)
    self.assertEqual(m.rfind(b'one', 0, -2), 0)
    self.assertEqual(m.rfind(b'one', 1, -1), 8)
    self.assertEqual(m.rfind(b'one', 1, -2), -1)
    self.assertEqual(m.rfind(bytearray(b'one')), 8)
