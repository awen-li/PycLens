# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_constructors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_constructors()
    self.assertEqual(tuple(), ())
    t0_3 = (0, 1, 2, 3)
    t0_3_bis = tuple(t0_3)
    self.assertTrue(t0_3 is t0_3_bis)
    self.assertEqual(tuple([]), ())
    self.assertEqual(tuple([0, 1, 2, 3]), (0, 1, 2, 3))
    self.assertEqual(tuple(''), ())
    self.assertEqual(tuple('spam'), ('s', 'p', 'a', 'm'))
    self.assertEqual(tuple((x for x in range(10) if x % 2)), (1, 3, 5, 7, 9))
