# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_extend

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    self.assertRaises(TypeError, a.extend)
    a.extend(array.array(self.typecode, self.example[::-1]))
    self.assertEqual(a, array.array(self.typecode, self.example + self.example[::-1]))
    a = array.array(self.typecode, self.example)
    a.extend(a)
    self.assertEqual(a, array.array(self.typecode, self.example + self.example))
    b = array.array(self.badtypecode())
    self.assertRaises(TypeError, a.extend, b)
    a = array.array(self.typecode, self.example)
    a.extend(self.example[::-1])
    self.assertEqual(a, array.array(self.typecode, self.example + self.example[::-1]))
