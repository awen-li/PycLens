# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    self.assertEntryEqual(a[0], self.example[0])
    self.assertEntryEqual(a[0], self.example[0])
    self.assertEntryEqual(a[-1], self.example[-1])
    self.assertEntryEqual(a[-1], self.example[-1])
    self.assertEntryEqual(a[len(self.example) - 1], self.example[-1])
    self.assertEntryEqual(a[-len(self.example)], self.example[0])
    self.assertRaises(TypeError, a.__getitem__)
    self.assertRaises(IndexError, a.__getitem__, len(self.example))
    self.assertRaises(IndexError, a.__getitem__, -len(self.example) - 1)
