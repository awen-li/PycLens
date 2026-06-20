# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_context_create_from_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    nc = self.decimal.Context()
    r = nc.create_decimal(0.1)
    self.assertEqual(type(r), Decimal)
    self.assertEqual(str(r), '0.1000000000000000055511151231')
    self.assertTrue(nc.create_decimal(float('nan')).is_qnan())
    self.assertTrue(nc.create_decimal(float('inf')).is_infinite())
    self.assertTrue(nc.create_decimal(float('-inf')).is_infinite())
    self.assertEqual(str(nc.create_decimal(float('nan'))), str(nc.create_decimal('NaN')))
    self.assertEqual(str(nc.create_decimal(float('inf'))), str(nc.create_decimal('Infinity')))
    self.assertEqual(str(nc.create_decimal(float('-inf'))), str(nc.create_decimal('-Infinity')))
    self.assertEqual(str(nc.create_decimal(float('-0.0'))), str(nc.create_decimal('-0')))
    nc.prec = 100
    for i in range(200):
        x = random.expovariate(0.01) * (random.random() * 2.0 - 1.0)
        self.assertEqual(x, float(nc.create_decimal(x)))
