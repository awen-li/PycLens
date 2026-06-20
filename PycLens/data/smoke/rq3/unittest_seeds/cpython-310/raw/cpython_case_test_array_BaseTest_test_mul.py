# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_mul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 5 * array.array(self.typecode, self.example)
    self.assertEqual(a, array.array(self.typecode, 5 * self.example))
    a = array.array(self.typecode, self.example) * 5
    self.assertEqual(a, array.array(self.typecode, self.example * 5))
    a = 0 * array.array(self.typecode, self.example)
    self.assertEqual(a, array.array(self.typecode))
    a = -1 * array.array(self.typecode, self.example)
    self.assertEqual(a, array.array(self.typecode))
    a = 5 * array.array(self.typecode, self.example[:1])
    self.assertEqual(a, array.array(self.typecode, [a[0]] * 5))
    self.assertRaises(TypeError, a.__mul__, 'bad')
