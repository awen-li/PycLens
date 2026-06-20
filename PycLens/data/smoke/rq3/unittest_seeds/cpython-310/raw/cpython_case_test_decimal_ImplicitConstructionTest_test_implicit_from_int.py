# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ImplicitConstructionTest_test_implicit_from_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertEqual(str(Decimal(5) + 45), '50')
    self.assertEqual(Decimal(5) + 123456789000, Decimal(123456789000))
