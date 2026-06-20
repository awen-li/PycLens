# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_rindex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'mississippi')
    i = 105
    w = 119
    self.assertEqual(b.rindex(b'ss'), 5)
    self.assertRaises(ValueError, b.rindex, b'w')
    self.assertRaises(ValueError, b.rindex, b'mississippian')
    self.assertEqual(b.rindex(i), 10)
    self.assertRaises(ValueError, b.rindex, w)
    self.assertEqual(b.rindex(b'ss', 3), 5)
    self.assertEqual(b.rindex(b'ss', 0, 6), 2)
    self.assertEqual(b.rindex(i, 1, 3), 1)
    self.assertEqual(b.rindex(i, 3, 9), 7)
    self.assertRaises(ValueError, b.rindex, w, 1, 3)
