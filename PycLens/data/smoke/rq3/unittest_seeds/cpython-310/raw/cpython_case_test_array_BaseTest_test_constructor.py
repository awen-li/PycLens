# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode)
    self.assertEqual(a.typecode, self.typecode)
    self.assertGreaterEqual(a.itemsize, self.minitemsize)
    self.assertRaises(TypeError, array.array, self.typecode, None)
