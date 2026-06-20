# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'mississippi')
    i = 105
    w = 119
    self.assertEqual(b.index(b'ss'), 2)
    self.assertRaises(ValueError, b.index, b'w')
    self.assertRaises(ValueError, b.index, b'mississippian')
    self.assertEqual(b.index(i), 1)
    self.assertRaises(ValueError, b.index, w)
    self.assertEqual(b.index(b'ss', 3), 5)
    self.assertEqual(b.index(b'ss', 1, 7), 2)
    self.assertRaises(ValueError, b.index, b'ss', 1, 3)
    self.assertEqual(b.index(i, 6), 7)
    self.assertEqual(b.index(i, 1, 3), 1)
    self.assertRaises(ValueError, b.index, w, 1, 3)
