# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_canonical

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    getcontext = self.decimal.getcontext
    x = Decimal(9).canonical()
    self.assertEqual(x, 9)
    c = getcontext()
    x = c.canonical(Decimal(9))
    self.assertEqual(x, 9)
