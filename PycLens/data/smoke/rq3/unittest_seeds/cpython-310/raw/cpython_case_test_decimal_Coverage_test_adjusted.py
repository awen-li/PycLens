# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_adjusted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertEqual(Decimal('1234e9999').adjusted(), 10002)
    self.assertEqual(Decimal('nan').adjusted(), 0)
    self.assertEqual(Decimal('inf').adjusted(), 0)
