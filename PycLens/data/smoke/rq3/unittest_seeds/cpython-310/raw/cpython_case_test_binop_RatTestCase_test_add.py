# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: RatTestCase_test_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Rat(2, 3) + Rat(1, 3), 1)
    self.assertEqual(Rat(2, 3) + 1, Rat(5, 3))
    self.assertEqual(1 + Rat(2, 3), Rat(5, 3))
    self.assertEqual(1.0 + Rat(1, 2), 1.5)
    self.assertEqual(Rat(1, 2) + 1.0, 1.5)
