# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_quantize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    InvalidOperation = self.decimal.InvalidOperation
    c = Context(Emax=99999, Emin=-99999)
    self.assertEqual(Decimal('7.335').quantize(Decimal('.01')), Decimal('7.34'))
    self.assertEqual(Decimal('7.335').quantize(Decimal('.01'), rounding=ROUND_DOWN), Decimal('7.33'))
    self.assertRaises(InvalidOperation, Decimal('10e99999').quantize, Decimal('1e100000'), context=c)
    c = Context()
    d = Decimal('0.871831e800')
    x = d.quantize(context=c, exp=Decimal('1e797'), rounding=ROUND_DOWN)
    self.assertEqual(x, Decimal('8.71E+799'))
