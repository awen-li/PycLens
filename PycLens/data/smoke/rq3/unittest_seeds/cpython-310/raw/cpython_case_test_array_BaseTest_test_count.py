# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = 2 * self.example
    a = array.array(self.typecode, example)
    self.assertRaises(TypeError, a.count)
    for x in example:
        self.assertEqual(a.count(x), example.count(x))
    self.assertEqual(a.count(self.outside), 0)
    self.assertEqual(a.count(None), 0)
