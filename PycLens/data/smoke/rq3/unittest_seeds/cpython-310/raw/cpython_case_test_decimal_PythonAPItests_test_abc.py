# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_abc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertTrue(issubclass(Decimal, numbers.Number))
    self.assertFalse(issubclass(Decimal, numbers.Real))
    self.assertIsInstance(Decimal(0), numbers.Number)
    self.assertNotIsInstance(Decimal(0), numbers.Real)
