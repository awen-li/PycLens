# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode)
    self.assertRaises(IndexError, a.pop)
    a = array.array(self.typecode, 2 * self.example)
    self.assertRaises(TypeError, a.pop, 42, 42)
    self.assertRaises(TypeError, a.pop, None)
    self.assertRaises(IndexError, a.pop, len(a))
    self.assertRaises(IndexError, a.pop, -len(a) - 1)
    self.assertEntryEqual(a.pop(0), self.example[0])
    self.assertEqual(a, array.array(self.typecode, self.example[1:] + self.example))
    self.assertEntryEqual(a.pop(1), self.example[2])
    self.assertEqual(a, array.array(self.typecode, self.example[1:2] + self.example[3:] + self.example))
    self.assertEntryEqual(a.pop(0), self.example[1])
    self.assertEntryEqual(a.pop(), self.example[-1])
    self.assertEqual(a, array.array(self.typecode, self.example[3:] + self.example[:-1]))
