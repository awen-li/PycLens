# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_nan_to_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    for s in ('nan', 'nan1234', '-nan', '-nan2468'):
        f = float(Decimal(s))
        self.assertTrue(math.isnan(f))
        sign = math.copysign(1.0, f)
        self.assertEqual(sign, -1.0 if s.startswith('-') else 1.0)
