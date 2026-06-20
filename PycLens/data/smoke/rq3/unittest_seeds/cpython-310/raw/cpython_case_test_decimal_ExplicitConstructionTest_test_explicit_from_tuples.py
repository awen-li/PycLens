# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_from_tuples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal((0, (0,), 0))
    self.assertEqual(str(d), '0')
    d = Decimal((1, (4, 5), 0))
    self.assertEqual(str(d), '-45')
    d = Decimal((0, (4, 5, 3, 4), -2))
    self.assertEqual(str(d), '45.34')
    d = Decimal((1, (4, 3, 4, 9, 1, 3, 5, 3, 4), -25))
    self.assertEqual(str(d), '-4.34913534E-17')
    d = Decimal((0, (), 'F'))
    self.assertEqual(str(d), 'Infinity')
    self.assertRaises(ValueError, Decimal, (1, (4, 3, 4, 9, 1)))
    self.assertRaises(ValueError, Decimal, (8, (4, 3, 4, 9, 1), 2))
    self.assertRaises(ValueError, Decimal, (0.0, (4, 3, 4, 9, 1), 2))
    self.assertRaises(ValueError, Decimal, (Decimal(1), (4, 3, 4, 9, 1), 2))
    self.assertRaises(ValueError, Decimal, (1, (4, 3, 4, 9, 1), 'wrong!'))
    self.assertRaises(ValueError, Decimal, (1, (4, 3, 4, 9, 1), 0.0))
    self.assertRaises(ValueError, Decimal, (1, (4, 3, 4, 9, 1), '1'))
    self.assertRaises(ValueError, Decimal, (1, 'xyz', 2))
    self.assertRaises(ValueError, Decimal, (1, (4, 3, 4, None, 1), 2))
    self.assertRaises(ValueError, Decimal, (1, (4, -3, 4, 9, 1), 2))
    self.assertRaises(ValueError, Decimal, (1, (4, 10, 4, 9, 1), 2))
    self.assertRaises(ValueError, Decimal, (1, (4, 3, 4, 'a', 1), 2))
