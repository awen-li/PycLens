# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: MiscTest_test_bad_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, array.array)
    self.assertRaises(TypeError, array.array, spam=42)
    self.assertRaises(TypeError, array.array, 'xx')
    self.assertRaises(ValueError, array.array, 'x')
