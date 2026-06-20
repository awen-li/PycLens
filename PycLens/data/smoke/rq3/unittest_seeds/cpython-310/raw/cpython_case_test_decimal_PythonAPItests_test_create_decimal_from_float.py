# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_create_decimal_from_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    Inexact = self.decimal.Inexact
    context = Context(prec=5, rounding=ROUND_DOWN)
    self.assertEqual(context.create_decimal_from_float(math.pi), Decimal('3.1415'))
    context = Context(prec=5, rounding=ROUND_UP)
    self.assertEqual(context.create_decimal_from_float(math.pi), Decimal('3.1416'))
    context = Context(prec=5, traps=[Inexact])
    self.assertRaises(Inexact, context.create_decimal_from_float, math.pi)
    self.assertEqual(repr(context.create_decimal_from_float(-0.0)), "Decimal('-0')")
    self.assertEqual(repr(context.create_decimal_from_float(1.0)), "Decimal('1')")
    self.assertEqual(repr(context.create_decimal_from_float(10)), "Decimal('10')")
