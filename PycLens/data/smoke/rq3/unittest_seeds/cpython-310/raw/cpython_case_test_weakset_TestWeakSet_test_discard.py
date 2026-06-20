# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_discard

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, q) = (ustr('a'), ustr('Q'))
    self.s.discard(a)
    self.assertNotIn(a, self.s)
    self.s.discard(q)
    self.assertRaises(TypeError, self.s.discard, [])
