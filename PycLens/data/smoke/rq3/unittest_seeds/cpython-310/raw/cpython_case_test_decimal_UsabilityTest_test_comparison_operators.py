# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_comparison_operators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    da = Decimal('23.42')
    db = Decimal('23.42')
    dc = Decimal('45')
    self.assertGreater(dc, da)
    self.assertGreaterEqual(dc, da)
    self.assertLess(da, dc)
    self.assertLessEqual(da, dc)
    self.assertEqual(da, db)
    self.assertNotEqual(da, dc)
    self.assertLessEqual(da, db)
    self.assertGreaterEqual(da, db)
    self.assertGreater(dc, 23)
    self.assertLess(23, dc)
    self.assertEqual(dc, 45)
    self.assertNotEqual(da, 'ugly')
    self.assertNotEqual(da, 32.7)
    self.assertNotEqual(da, object())
    self.assertNotEqual(da, object)
    a = list(map(Decimal, range(100)))
    b = a[:]
    random.shuffle(a)
    a.sort()
    self.assertEqual(a, b)
