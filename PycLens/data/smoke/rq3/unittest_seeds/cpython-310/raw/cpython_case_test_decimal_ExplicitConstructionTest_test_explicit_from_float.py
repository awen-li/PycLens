# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_from_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    r = Decimal(0.1)
    self.assertEqual(type(r), Decimal)
    self.assertEqual(str(r), '0.1000000000000000055511151231257827021181583404541015625')
    self.assertTrue(Decimal(float('nan')).is_qnan())
    self.assertTrue(Decimal(float('inf')).is_infinite())
    self.assertTrue(Decimal(float('-inf')).is_infinite())
    self.assertEqual(str(Decimal(float('nan'))), str(Decimal('NaN')))
    self.assertEqual(str(Decimal(float('inf'))), str(Decimal('Infinity')))
    self.assertEqual(str(Decimal(float('-inf'))), str(Decimal('-Infinity')))
    self.assertEqual(str(Decimal(float('-0.0'))), str(Decimal('-0')))
    for i in range(200):
        x = random.expovariate(0.01) * (random.random() * 2.0 - 1.0)
        self.assertEqual(x, float(Decimal(x)))
