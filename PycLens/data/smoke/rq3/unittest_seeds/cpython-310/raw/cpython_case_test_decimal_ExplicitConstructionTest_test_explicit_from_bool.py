# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_from_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertIs(bool(Decimal(0)), False)
    self.assertIs(bool(Decimal(1)), True)
    self.assertEqual(Decimal(False), Decimal(0))
    self.assertEqual(Decimal(True), Decimal(1))
