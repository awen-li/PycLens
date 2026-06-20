# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: MemoryBIOTests_test_pending

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = ssl.MemoryBIO()
    self.assertEqual(bio.pending, 0)
    bio.write(b'foo')
    self.assertEqual(bio.pending, 3)
    for i in range(3):
        bio.read(1)
        self.assertEqual(bio.pending, 3 - i - 1)
    for i in range(3):
        bio.write(b'x')
        self.assertEqual(bio.pending, i + 1)
    bio.read()
    self.assertEqual(bio.pending, 0)
