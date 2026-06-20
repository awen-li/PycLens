# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_from_Decimal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal(45)
    e = Decimal(d)
    self.assertEqual(str(e), '45')
    d = Decimal(500000123)
    e = Decimal(d)
    self.assertEqual(str(e), '500000123')
    d = Decimal(-45)
    e = Decimal(d)
    self.assertEqual(str(e), '-45')
    d = Decimal(0)
    e = Decimal(d)
    self.assertEqual(str(e), '0')
