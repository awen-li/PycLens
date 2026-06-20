# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l0 = tuple()
    l2 = (0, 1, 2)
    a0 = self.type2test(l0)
    a2 = self.type2test(l2)
    self.assertEqual(str(a0), repr(l0))
    self.assertEqual(str(a2), repr(l2))
    self.assertEqual(repr(a0), '()')
    self.assertEqual(repr(a2), '(0, 1, 2)')
