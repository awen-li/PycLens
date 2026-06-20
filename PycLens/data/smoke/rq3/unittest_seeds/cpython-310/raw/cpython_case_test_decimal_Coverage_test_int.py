# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    localcontext = self.decimal.localcontext
    with localcontext() as c:
        c.prec = 9999
        x = Decimal(1221 ** 1271) / 10 ** 3923
        self.assertEqual(int(x), 1)
        self.assertEqual(x.to_integral(), 2)
