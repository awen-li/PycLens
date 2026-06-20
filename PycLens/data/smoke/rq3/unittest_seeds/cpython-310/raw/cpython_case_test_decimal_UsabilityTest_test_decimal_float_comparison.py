# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_decimal_float_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    da = Decimal('0.25')
    db = Decimal('3.0')
    self.assertLess(da, 3.0)
    self.assertLessEqual(da, 3.0)
    self.assertGreater(db, 0.25)
    self.assertGreaterEqual(db, 0.25)
    self.assertNotEqual(da, 1.5)
    self.assertEqual(da, 0.25)
    self.assertGreater(3.0, da)
    self.assertGreaterEqual(3.0, da)
    self.assertLess(0.25, db)
    self.assertLessEqual(0.25, db)
    self.assertNotEqual(0.25, db)
    self.assertEqual(3.0, db)
    self.assertNotEqual(0.1, Decimal('0.1'))
