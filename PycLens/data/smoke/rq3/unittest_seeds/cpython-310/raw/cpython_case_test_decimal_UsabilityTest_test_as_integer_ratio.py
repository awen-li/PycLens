# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_as_integer_ratio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertRaises(OverflowError, Decimal.as_integer_ratio, Decimal('inf'))
    self.assertRaises(OverflowError, Decimal.as_integer_ratio, Decimal('-inf'))
    self.assertRaises(ValueError, Decimal.as_integer_ratio, Decimal('-nan'))
    self.assertRaises(ValueError, Decimal.as_integer_ratio, Decimal('snan123'))
    for exp in range(-4, 2):
        for coeff in range(1000):
            for sign in ('+', '-'):
                d = Decimal('%s%dE%d' % (sign, coeff, exp))
                pq = d.as_integer_ratio()
                (p, q) = pq
                self.assertIsInstance(pq, tuple)
                self.assertIsInstance(p, int)
                self.assertIsInstance(q, int)
                self.assertGreater(q, 0)
                self.assertEqual(math.gcd(p, q), 1)
                self.assertEqual(Decimal(p) / Decimal(q), d)
