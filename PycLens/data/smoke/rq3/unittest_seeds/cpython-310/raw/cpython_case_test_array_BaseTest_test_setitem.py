# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    a[0] = a[-1]
    self.assertEntryEqual(a[0], a[-1])
    a = array.array(self.typecode, self.example)
    a[0] = a[-1]
    self.assertEntryEqual(a[0], a[-1])
    a = array.array(self.typecode, self.example)
    a[-1] = a[0]
    self.assertEntryEqual(a[0], a[-1])
    a = array.array(self.typecode, self.example)
    a[-1] = a[0]
    self.assertEntryEqual(a[0], a[-1])
    a = array.array(self.typecode, self.example)
    a[len(self.example) - 1] = a[0]
    self.assertEntryEqual(a[0], a[-1])
    a = array.array(self.typecode, self.example)
    a[-len(self.example)] = a[-1]
    self.assertEntryEqual(a[0], a[-1])
    self.assertRaises(TypeError, a.__setitem__)
    self.assertRaises(TypeError, a.__setitem__, None)
    self.assertRaises(TypeError, a.__setitem__, 0, None)
    self.assertRaises(IndexError, a.__setitem__, len(self.example), self.example[0])
    self.assertRaises(IndexError, a.__setitem__, -len(self.example) - 1, self.example[0])
