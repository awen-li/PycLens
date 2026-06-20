# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    del a[0]
    self.assertEqual(a, array.array(self.typecode, self.example[1:]))
    a = array.array(self.typecode, self.example)
    del a[-1]
    self.assertEqual(a, array.array(self.typecode, self.example[:-1]))
    a = array.array(self.typecode, self.example)
    del a[len(self.example) - 1]
    self.assertEqual(a, array.array(self.typecode, self.example[:-1]))
    a = array.array(self.typecode, self.example)
    del a[-len(self.example)]
    self.assertEqual(a, array.array(self.typecode, self.example[1:]))
    self.assertRaises(TypeError, a.__delitem__)
    self.assertRaises(TypeError, a.__delitem__, None)
    self.assertRaises(IndexError, a.__delitem__, len(self.example))
    self.assertRaises(IndexError, a.__delitem__, -len(self.example) - 1)
