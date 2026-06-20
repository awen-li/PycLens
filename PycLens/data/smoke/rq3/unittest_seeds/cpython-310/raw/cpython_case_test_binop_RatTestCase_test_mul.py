# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: RatTestCase_test_mul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Rat(2, 3) * Rat(5, 7), Rat(10, 21))
    self.assertEqual(Rat(10, 3) * 3, 10)
    self.assertEqual(3 * Rat(10, 3), 10)
    self.assertEqual(Rat(10, 5) * 0.5, 1.0)
    self.assertEqual(0.5 * Rat(10, 5), 1.0)
