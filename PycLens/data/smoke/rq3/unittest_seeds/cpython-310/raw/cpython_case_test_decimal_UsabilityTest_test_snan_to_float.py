# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_snan_to_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    for s in ('snan', '-snan', 'snan1357', '-snan1234'):
        d = Decimal(s)
        self.assertRaises(ValueError, float, d)
