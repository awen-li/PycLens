# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: RatTestCase_test_true_div

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Rat(10, 3) / Rat(5, 7), Rat(14, 3))
    self.assertEqual(Rat(10, 3) / 3, Rat(10, 9))
    self.assertEqual(2 / Rat(5), Rat(2, 5))
    self.assertEqual(3.0 * Rat(1, 2), 1.5)
    self.assertEqual(Rat(1, 2) * 3.0, 1.5)
    self.assertEqual(eval('1/2'), 0.5)
