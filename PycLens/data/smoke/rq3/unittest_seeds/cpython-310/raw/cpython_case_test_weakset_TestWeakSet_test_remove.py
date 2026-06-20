# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_remove

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ustr('a')
    self.s.remove(x)
    self.assertNotIn(x, self.s)
    self.assertRaises(KeyError, self.s.remove, x)
    self.assertRaises(TypeError, self.s.remove, [])
