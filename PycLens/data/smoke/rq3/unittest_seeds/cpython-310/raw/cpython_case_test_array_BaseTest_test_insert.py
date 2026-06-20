# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_insert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    a.insert(0, self.example[0])
    self.assertEqual(len(a), 1 + len(self.example))
    self.assertEqual(a[0], a[1])
    self.assertRaises(TypeError, a.insert)
    self.assertRaises(TypeError, a.insert, None)
    self.assertRaises(TypeError, a.insert, 0, None)
    a = array.array(self.typecode, self.example)
    a.insert(-1, self.example[0])
    self.assertEqual(a, array.array(self.typecode, self.example[:-1] + self.example[:1] + self.example[-1:]))
    a = array.array(self.typecode, self.example)
    a.insert(-1000, self.example[0])
    self.assertEqual(a, array.array(self.typecode, self.example[:1] + self.example))
    a = array.array(self.typecode, self.example)
    a.insert(1000, self.example[0])
    self.assertEqual(a, array.array(self.typecode, self.example + self.example[:1]))
