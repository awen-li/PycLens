# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_equality_with_other_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertIn(Decimal(10), ['a', 1.0, Decimal(10), (1, 2), {}])
    self.assertNotIn(Decimal(10), ['a', 1.0, (1, 2), {}])
