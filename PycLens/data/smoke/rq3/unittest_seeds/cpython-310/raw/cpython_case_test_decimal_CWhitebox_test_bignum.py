# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_bignum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    localcontext = C.localcontext
    b1 = 10 ** 35
    b2 = 10 ** 36
    with localcontext() as c:
        c.prec = 1000000
        for i in range(5):
            a = random.randrange(b1, b2)
            b = random.randrange(1000, 1200)
            x = a ** b
            y = Decimal(a) ** Decimal(b)
            self.assertEqual(x, y)
