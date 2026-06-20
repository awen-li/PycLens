# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_tofromlist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, 2 * self.example)
    b = array.array(self.typecode)
    self.assertRaises(TypeError, a.tolist, 42)
    self.assertRaises(TypeError, b.fromlist)
    self.assertRaises(TypeError, b.fromlist, 42)
    self.assertRaises(TypeError, b.fromlist, [None])
    b.fromlist(a.tolist())
    self.assertEqual(a, b)
