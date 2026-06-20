# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_tonum_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d1 = Decimal('66')
    d2 = Decimal('15.32')
    self.assertEqual(int(d1), 66)
    self.assertEqual(int(d2), 15)
    self.assertEqual(float(d1), 66)
    self.assertEqual(float(d2), 15.32)
    test_pairs = [('123.00', 123), ('3.2', 3), ('3.54', 3), ('3.899', 3), ('-2.3', -3), ('-11.0', -11), ('0.0', 0), ('-0E3', 0), ('89891211712379812736.1', 89891211712379812736)]
    for (d, i) in test_pairs:
        self.assertEqual(math.floor(Decimal(d)), i)
    self.assertRaises(ValueError, math.floor, Decimal('-NaN'))
    self.assertRaises(ValueError, math.floor, Decimal('sNaN'))
    self.assertRaises(ValueError, math.floor, Decimal('NaN123'))
    self.assertRaises(OverflowError, math.floor, Decimal('Inf'))
    self.assertRaises(OverflowError, math.floor, Decimal('-Inf'))
    test_pairs = [('123.00', 123), ('3.2', 4), ('3.54', 4), ('3.899', 4), ('-2.3', -2), ('-11.0', -11), ('0.0', 0), ('-0E3', 0), ('89891211712379812736.1', 89891211712379812737)]
    for (d, i) in test_pairs:
        self.assertEqual(math.ceil(Decimal(d)), i)
    self.assertRaises(ValueError, math.ceil, Decimal('-NaN'))
    self.assertRaises(ValueError, math.ceil, Decimal('sNaN'))
    self.assertRaises(ValueError, math.ceil, Decimal('NaN123'))
    self.assertRaises(OverflowError, math.ceil, Decimal('Inf'))
    self.assertRaises(OverflowError, math.ceil, Decimal('-Inf'))
    test_pairs = [('123.00', 123), ('3.2', 3), ('3.54', 4), ('3.899', 4), ('-2.3', -2), ('-11.0', -11), ('0.0', 0), ('-0E3', 0), ('-3.5', -4), ('-2.5', -2), ('-1.5', -2), ('-0.5', 0), ('0.5', 0), ('1.5', 2), ('2.5', 2), ('3.5', 4)]
    for (d, i) in test_pairs:
        self.assertEqual(round(Decimal(d)), i)
    self.assertRaises(ValueError, round, Decimal('-NaN'))
    self.assertRaises(ValueError, round, Decimal('sNaN'))
    self.assertRaises(ValueError, round, Decimal('NaN123'))
    self.assertRaises(OverflowError, round, Decimal('Inf'))
    self.assertRaises(OverflowError, round, Decimal('-Inf'))
    test_triples = [('123.456', -4, '0E+4'), ('123.456', -3, '0E+3'), ('123.456', -2, '1E+2'), ('123.456', -1, '1.2E+2'), ('123.456', 0, '123'), ('123.456', 1, '123.5'), ('123.456', 2, '123.46'), ('123.456', 3, '123.456'), ('123.456', 4, '123.4560'), ('123.455', 2, '123.46'), ('123.445', 2, '123.44'), ('Inf', 4, 'NaN'), ('-Inf', -23, 'NaN'), ('sNaN314', 3, 'NaN314')]
    for (d, n, r) in test_triples:
        self.assertEqual(str(round(Decimal(d), n)), r)
