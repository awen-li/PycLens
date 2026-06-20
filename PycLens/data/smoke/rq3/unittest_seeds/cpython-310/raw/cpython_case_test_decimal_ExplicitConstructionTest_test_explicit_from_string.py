# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ExplicitConstructionTest_test_explicit_from_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    InvalidOperation = self.decimal.InvalidOperation
    localcontext = self.decimal.localcontext
    self.assertEqual(str(Decimal('')), 'NaN')
    self.assertEqual(str(Decimal('45')), '45')
    self.assertEqual(str(Decimal('45.34')), '45.34')
    self.assertEqual(str(Decimal('45e2')), '4.5E+3')
    self.assertEqual(str(Decimal('ugly')), 'NaN')
    self.assertEqual(str(Decimal('1.3E4 \n')), '1.3E+4')
    self.assertEqual(str(Decimal('  -7.89')), '-7.89')
    self.assertEqual(str(Decimal('  3.45679  ')), '3.45679')
    self.assertEqual(str(Decimal('1_3.3e4_0')), '1.33E+41')
    self.assertEqual(str(Decimal('1_0_0_0')), '1000')
    for lead in ['', ' ', '\xa0', '\u205f']:
        for trail in ['', ' ', '\xa0', '\u205f']:
            self.assertEqual(str(Decimal(lead + '9.311E+28' + trail)), '9.311E+28')
    with localcontext() as c:
        c.traps[InvalidOperation] = True
        self.assertRaises(InvalidOperation, Decimal, 'xyz')
        self.assertRaises(TypeError, Decimal, '1234', 'x', 'y')
        self.assertRaises(InvalidOperation, Decimal, '1\xa02\xa03')
        self.assertRaises(InvalidOperation, Decimal, '\xa01\xa02\xa0')
        self.assertRaises(InvalidOperation, Decimal, '\xa0')
        self.assertRaises(InvalidOperation, Decimal, '\xa0\xa0')
        self.assertRaises(InvalidOperation, Decimal, '12\x003')
        self.assertRaises(InvalidOperation, Decimal, '1_2_\x003')
