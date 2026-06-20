# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_as_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d = Decimal(0)
    self.assertEqual(d.as_tuple(), (0, (0,), 0))
    d = Decimal(-45)
    self.assertEqual(d.as_tuple(), (1, (4, 5), 0))
    d = Decimal('-4.34913534E-17')
    self.assertEqual(d.as_tuple(), (1, (4, 3, 4, 9, 1, 3, 5, 3, 4), -25))
    d = Decimal('Infinity')
    self.assertEqual(d.as_tuple(), (0, (0,), 'F'))
    d = Decimal((0, (0, 0, 4, 0, 5, 3, 4), -2))
    self.assertEqual(d.as_tuple(), (0, (4, 0, 5, 3, 4), -2))
    d = Decimal((1, (0, 0, 0), 37))
    self.assertEqual(d.as_tuple(), (1, (0,), 37))
    d = Decimal((1, (), 37))
    self.assertEqual(d.as_tuple(), (1, (0,), 37))
    d = Decimal((0, (0, 0, 4, 0, 5, 3, 4), 'n'))
    self.assertEqual(d.as_tuple(), (0, (4, 0, 5, 3, 4), 'n'))
    d = Decimal((1, (0, 0, 0), 'N'))
    self.assertEqual(d.as_tuple(), (1, (), 'N'))
    d = Decimal((1, (), 'n'))
    self.assertEqual(d.as_tuple(), (1, (), 'n'))
    d = Decimal((0, (0,), 'F'))
    self.assertEqual(d.as_tuple(), (0, (0,), 'F'))
    d = Decimal((0, (4, 5, 3, 4), 'F'))
    self.assertEqual(d.as_tuple(), (0, (0,), 'F'))
    d = Decimal((1, (0, 2, 7, 1), 'F'))
    self.assertEqual(d.as_tuple(), (1, (0,), 'F'))
