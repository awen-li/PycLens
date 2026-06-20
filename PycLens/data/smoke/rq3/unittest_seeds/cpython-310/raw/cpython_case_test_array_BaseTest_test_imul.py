# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_imul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    b = a
    a *= 5
    self.assertIs(a, b)
    self.assertEqual(a, array.array(self.typecode, 5 * self.example))
    a *= 0
    self.assertIs(a, b)
    self.assertEqual(a, array.array(self.typecode))
    a *= 1000
    self.assertIs(a, b)
    self.assertEqual(a, array.array(self.typecode))
    a *= -1
    self.assertIs(a, b)
    self.assertEqual(a, array.array(self.typecode))
    a = array.array(self.typecode, self.example)
    a *= -1
    self.assertEqual(a, array.array(self.typecode))
    self.assertRaises(TypeError, a.__imul__, 'bad')
