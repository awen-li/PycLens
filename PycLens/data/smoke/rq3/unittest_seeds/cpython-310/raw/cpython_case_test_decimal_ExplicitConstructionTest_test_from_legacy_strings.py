# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_from_legacy_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    Decimal = self.decimal.Decimal
    context = self.decimal.Context()
    s = _testcapi.unicode_legacy_string('9.999999')
    self.assertEqual(str(Decimal(s)), '9.999999')
    self.assertEqual(str(context.create_decimal(s)), '9.999999')
