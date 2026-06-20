# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = 2 * self.example
    a = array.array(self.typecode, example)
    self.assertRaises(TypeError, a.index)
    for x in example:
        self.assertEqual(a.index(x), example.index(x))
    self.assertRaises(ValueError, a.index, None)
    self.assertRaises(ValueError, a.index, self.outside)
    a = array.array('i', [-2, -1, 0, 0, 1, 2])
    self.assertEqual(a.index(0), 2)
    self.assertEqual(a.index(0, 2), 2)
    self.assertEqual(a.index(0, -4), 2)
    self.assertEqual(a.index(-2, -10), 0)
    self.assertEqual(a.index(0, 3), 3)
    self.assertEqual(a.index(0, -3), 3)
    self.assertEqual(a.index(0, 3, 4), 3)
    self.assertEqual(a.index(0, -3, -2), 3)
    self.assertRaises(ValueError, a.index, 2, 0, -10)
