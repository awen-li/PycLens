# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal

    class MyDecimal(Decimal):
        y = None
    d1 = MyDecimal(1)
    d2 = MyDecimal(2)
    d = d1 + d2
    self.assertIs(type(d), Decimal)
    d = d1.max(d2)
    self.assertIs(type(d), Decimal)
    d = copy.copy(d1)
    self.assertIs(type(d), MyDecimal)
    self.assertEqual(d, d1)
    d = copy.deepcopy(d1)
    self.assertIs(type(d), MyDecimal)
    self.assertEqual(d, d1)
    d = Decimal('1.0')
    x = Decimal(d)
    self.assertIs(type(x), Decimal)
    self.assertEqual(x, d)
    m = MyDecimal(d)
    self.assertIs(type(m), MyDecimal)
    self.assertEqual(m, d)
    self.assertIs(m.y, None)
    x = Decimal(m)
    self.assertIs(type(x), Decimal)
    self.assertEqual(x, d)
    m.y = 9
    x = MyDecimal(m)
    self.assertIs(type(x), MyDecimal)
    self.assertEqual(x, d)
    self.assertIs(x.y, None)
