# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: StringTest_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_setitem()
    a = array.array(self.typecode, self.example)
    self.assertRaises(TypeError, a.__setitem__, 0, self.example[:2])
