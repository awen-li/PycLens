# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_iadd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example[::-1])
    b = a
    a += array.array(self.typecode, 2 * self.example)
    self.assertIs(a, b)
    self.assertEqual(a, array.array(self.typecode, self.example[::-1] + 2 * self.example))
    a = array.array(self.typecode, self.example)
    a += a
    self.assertEqual(a, array.array(self.typecode, self.example + self.example))
    b = array.array(self.badtypecode())
    self.assertRaises(TypeError, a.__add__, b)
    self.assertRaises(TypeError, a.__iadd__, 'bad')
