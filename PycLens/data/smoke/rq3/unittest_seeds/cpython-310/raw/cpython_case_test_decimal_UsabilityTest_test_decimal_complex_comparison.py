# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_decimal_complex_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    da = Decimal('0.25')
    db = Decimal('3.0')
    self.assertNotEqual(da, 1.5 + 0j)
    self.assertNotEqual(1.5 + 0j, da)
    self.assertEqual(da, 0.25 + 0j)
    self.assertEqual(0.25 + 0j, da)
    self.assertEqual(3.0 + 0j, db)
    self.assertEqual(db, 3.0 + 0j)
    self.assertNotEqual(db, 3.0 + 1j)
    self.assertNotEqual(3.0 + 1j, db)
    self.assertIs(db.__lt__(3.0 + 0j), NotImplemented)
    self.assertIs(db.__le__(3.0 + 0j), NotImplemented)
    self.assertIs(db.__gt__(3.0 + 0j), NotImplemented)
    self.assertIs(db.__le__(3.0 + 0j), NotImplemented)
