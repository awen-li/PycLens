# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: PythonAPItests_test_from_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal

    class MyDecimal(Decimal):

        def __init__(self, _):
            self.x = 'y'
    self.assertTrue(issubclass(MyDecimal, Decimal))
    r = MyDecimal.from_float(0.1)
    self.assertEqual(type(r), MyDecimal)
    self.assertEqual(str(r), '0.1000000000000000055511151231257827021181583404541015625')
    self.assertEqual(r.x, 'y')
    bigint = 12345678901234567890123456789
    self.assertEqual(MyDecimal.from_float(bigint), MyDecimal(bigint))
    self.assertTrue(MyDecimal.from_float(float('nan')).is_qnan())
    self.assertTrue(MyDecimal.from_float(float('inf')).is_infinite())
    self.assertTrue(MyDecimal.from_float(float('-inf')).is_infinite())
    self.assertEqual(str(MyDecimal.from_float(float('nan'))), str(Decimal('NaN')))
    self.assertEqual(str(MyDecimal.from_float(float('inf'))), str(Decimal('Infinity')))
    self.assertEqual(str(MyDecimal.from_float(float('-inf'))), str(Decimal('-Infinity')))
    self.assertRaises(TypeError, MyDecimal.from_float, 'abc')
    for i in range(200):
        x = random.expovariate(0.01) * (random.random() * 2.0 - 1.0)
        self.assertEqual(x, float(MyDecimal.from_float(x)))
