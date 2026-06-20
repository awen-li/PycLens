# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_remove

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in self.example:
        example = 2 * self.example
        a = array.array(self.typecode, example)
        pos = example.index(x)
        example2 = example[:pos] + example[pos + 1:]
        a.remove(x)
        self.assertEqual(a, array.array(self.typecode, example2))
    a = array.array(self.typecode, self.example)
    self.assertRaises(ValueError, a.remove, self.outside)
    self.assertRaises(ValueError, a.remove, None)
