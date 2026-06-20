# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: EnumerateTestCase_test_argumentcheck

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.enum)
    self.assertRaises(TypeError, self.enum, 1)
    self.assertRaises(TypeError, self.enum, 'abc', 'a')
    self.assertRaises(TypeError, self.enum, 'abc', 2, 3)
