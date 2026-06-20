# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: StrTest_test_repr_small

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '-' * size
    s = repr(s)
    self.assertEqual(len(s), size + 2)
    self.assertEqual(s[0], "'")
    self.assertEqual(s[-1], "'")
    self.assertEqual(s.count('-'), size)
    del s
    size = size // 5 * 2
    s = '\x00' * size
    s = repr(s)
    self.assertEqual(len(s), size * 4 + 2)
    self.assertEqual(s[0], "'")
    self.assertEqual(s[-1], "'")
    self.assertEqual(s.count('\\'), size)
    self.assertEqual(s.count('0'), size * 2)
