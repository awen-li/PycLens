# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b1 = self.type2test([1, 2, 3])
    b2 = self.type2test([1, 2, 3])
    b3 = self.type2test([1, 3])
    self.assertEqual(b1, b2)
    self.assertTrue(b2 != b3)
    self.assertTrue(b1 <= b2)
    self.assertTrue(b1 <= b3)
    self.assertTrue(b1 < b3)
    self.assertTrue(b1 >= b2)
    self.assertTrue(b3 >= b2)
    self.assertTrue(b3 > b2)
    self.assertFalse(b1 != b2)
    self.assertFalse(b2 == b3)
    self.assertFalse(b1 > b2)
    self.assertFalse(b1 > b3)
    self.assertFalse(b1 >= b3)
    self.assertFalse(b1 < b2)
    self.assertFalse(b3 < b2)
    self.assertFalse(b3 <= b2)
