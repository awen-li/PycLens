# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_lexicographic_ordering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = self.type2test([1, 2])
    b = self.type2test([1, 2, 0])
    c = self.type2test([1, 3])
    self.assertLess(a, b)
    self.assertLess(b, c)
