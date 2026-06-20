# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'mississippi')
    i = 105
    p = 112
    w = 119
    self.assertEqual(b.count(b'i'), 4)
    self.assertEqual(b.count(b'ss'), 2)
    self.assertEqual(b.count(b'w'), 0)
    self.assertEqual(b.count(i), 4)
    self.assertEqual(b.count(w), 0)
    self.assertEqual(b.count(b'i', 6), 2)
    self.assertEqual(b.count(b'p', 6), 2)
    self.assertEqual(b.count(b'i', 1, 3), 1)
    self.assertEqual(b.count(b'p', 7, 9), 1)
    self.assertEqual(b.count(i, 6), 2)
    self.assertEqual(b.count(p, 6), 2)
    self.assertEqual(b.count(i, 1, 3), 1)
    self.assertEqual(b.count(p, 7, 9), 1)
