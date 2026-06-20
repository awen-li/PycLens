# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_radix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    getcontext = self.decimal.getcontext
    c = getcontext()
    self.assertEqual(Decimal('1').radix(), 10)
    self.assertEqual(c.radix(), 10)
