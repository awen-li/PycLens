# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_min_and_max_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d1 = Decimal('15.32')
    d2 = Decimal('28.5')
    l1 = 15
    l2 = 28
    self.assertIs(min(d1, d2), d1)
    self.assertIs(min(d2, d1), d1)
    self.assertIs(max(d1, d2), d2)
    self.assertIs(max(d2, d1), d2)
    self.assertIs(min(d1, l2), d1)
    self.assertIs(min(l2, d1), d1)
    self.assertIs(max(l1, d2), d2)
    self.assertIs(max(d2, l1), d2)
