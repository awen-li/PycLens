# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ArithmeticOperatorsTest_test_unary_operators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertEqual(+Decimal(45), Decimal(+45))
    self.assertEqual(-Decimal(45), Decimal(-45))
    self.assertEqual(abs(Decimal(45)), abs(Decimal(-45)))
