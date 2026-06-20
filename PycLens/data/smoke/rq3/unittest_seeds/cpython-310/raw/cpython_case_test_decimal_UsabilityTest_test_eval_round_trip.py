# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_eval_round_trip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal((0, (0,), 0))
    self.assertEqual(d, eval(repr(d)))
    d = Decimal((1, (4, 5), 0))
    self.assertEqual(d, eval(repr(d)))
    d = Decimal((0, (4, 5, 3, 4), -2))
    self.assertEqual(d, eval(repr(d)))
    d = Decimal((1, (4, 3, 4, 9, 1, 3, 5, 3, 4), -25))
    self.assertEqual(d, eval(repr(d)))
