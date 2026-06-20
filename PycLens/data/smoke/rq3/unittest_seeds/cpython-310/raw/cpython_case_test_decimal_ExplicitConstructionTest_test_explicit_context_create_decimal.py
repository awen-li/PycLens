# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_context_create_decimal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    InvalidOperation = self.decimal.InvalidOperation
    Rounded = self.decimal.Rounded
    nc = copy.copy(self.decimal.getcontext())
    nc.prec = 3
    d = Decimal()
    self.assertEqual(str(d), '0')
    d = nc.create_decimal()
    self.assertEqual(str(d), '0')
    self.assertRaises(TypeError, nc.create_decimal, None)
    d = nc.create_decimal(456)
    self.assertIsInstance(d, Decimal)
    self.assertEqual(nc.create_decimal(45678), nc.create_decimal('457E+2'))
    d = Decimal('456789')
    self.assertEqual(str(d), '456789')
    d = nc.create_decimal('456789')
    self.assertEqual(str(d), '4.57E+5')
    self.assertEqual(str(nc.create_decimal('3.14\n')), 'NaN')
    d = Decimal((1, (4, 3, 4, 9, 1, 3, 5, 3, 4), -25))
    self.assertEqual(str(d), '-4.34913534E-17')
    d = nc.create_decimal((1, (4, 3, 4, 9, 1, 3, 5, 3, 4), -25))
    self.assertEqual(str(d), '-4.35E-17')
    prevdec = Decimal(500000123)
    d = Decimal(prevdec)
    self.assertEqual(str(d), '500000123')
    d = nc.create_decimal(prevdec)
    self.assertEqual(str(d), '5.00E+8')
    nc.prec = 28
    nc.traps[InvalidOperation] = True
    for v in [-2 ** 63 - 1, -2 ** 63, -2 ** 31 - 1, -2 ** 31, 0, 2 ** 31 - 1, 2 ** 31, 2 ** 63 - 1, 2 ** 63]:
        d = nc.create_decimal(v)
        self.assertTrue(isinstance(d, Decimal))
        self.assertEqual(int(d), v)
    nc.prec = 3
    nc.traps[Rounded] = True
    self.assertRaises(Rounded, nc.create_decimal, 1234)
    nc.prec = 28
    self.assertEqual(str(nc.create_decimal('0E-017')), '0E-17')
    self.assertEqual(str(nc.create_decimal('45')), '45')
    self.assertEqual(str(nc.create_decimal('-Inf')), '-Infinity')
    self.assertEqual(str(nc.create_decimal('NaN123')), 'NaN123')
    self.assertRaises(InvalidOperation, nc.create_decimal, 'xyz')
    self.assertRaises(ValueError, nc.create_decimal, (1, 'xyz', -25))
    self.assertRaises(TypeError, nc.create_decimal, '1234', '5678')
    self.assertRaises(InvalidOperation, nc.create_decimal, ' 1234')
    self.assertRaises(InvalidOperation, nc.create_decimal, '12_34')
    nc.prec = 3
    self.assertRaises(InvalidOperation, nc.create_decimal, 'NaN12345')
    self.assertRaises(InvalidOperation, nc.create_decimal, Decimal('NaN12345'))
    nc.traps[InvalidOperation] = False
    self.assertEqual(str(nc.create_decimal('NaN12345')), 'NaN')
    self.assertTrue(nc.flags[InvalidOperation])
    nc.flags[InvalidOperation] = False
    self.assertEqual(str(nc.create_decimal(Decimal('NaN12345'))), 'NaN')
    self.assertTrue(nc.flags[InvalidOperation])
