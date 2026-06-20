# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_unicode_digits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    test_values = {'１': '1', '٠.٠٣٧٢e-٣': '0.0000372', '-nan౨౪౦౦': '-NaN2400'}
    for (input, expected) in test_values.items():
        self.assertEqual(str(Decimal(input)), expected)
