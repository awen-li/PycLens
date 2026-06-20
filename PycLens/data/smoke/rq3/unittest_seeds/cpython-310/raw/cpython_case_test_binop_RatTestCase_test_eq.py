# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binop.py
# case: RatTestCase_test_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Rat(10), Rat(20, 2))
    self.assertEqual(Rat(10), 10)
    self.assertEqual(10, Rat(10))
    self.assertEqual(Rat(10), 10.0)
    self.assertEqual(10.0, Rat(10))
