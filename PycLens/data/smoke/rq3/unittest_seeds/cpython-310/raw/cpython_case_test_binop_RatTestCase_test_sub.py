# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: RatTestCase_test_sub

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Rat(7, 2) - Rat(7, 5), Rat(21, 10))
    self.assertEqual(Rat(7, 5) - 1, Rat(2, 5))
    self.assertEqual(1 - Rat(3, 5), Rat(2, 5))
    self.assertEqual(Rat(3, 2) - 1.0, 0.5)
    self.assertEqual(1.0 - Rat(1, 2), 0.5)
