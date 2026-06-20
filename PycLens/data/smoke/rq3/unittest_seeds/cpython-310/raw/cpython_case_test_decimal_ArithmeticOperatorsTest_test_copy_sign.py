# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ArithmeticOperatorsTest_test_copy_sign

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal(1).copy_sign(Decimal(-2))
    self.assertEqual(Decimal(1).copy_sign(-2), d)
    self.assertRaises(TypeError, Decimal(1).copy_sign, '-2')
