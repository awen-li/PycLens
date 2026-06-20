# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_from_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal(45)
    self.assertEqual(str(d), '45')
    d = Decimal(500000123)
    self.assertEqual(str(d), '500000123')
    d = Decimal(-45)
    self.assertEqual(str(d), '-45')
    d = Decimal(0)
    self.assertEqual(str(d), '0')
    for n in range(0, 32):
        for sign in (-1, 1):
            for x in range(-5, 5):
                i = sign * (2 ** n + x)
                d = Decimal(i)
                self.assertEqual(str(d), str(i))
