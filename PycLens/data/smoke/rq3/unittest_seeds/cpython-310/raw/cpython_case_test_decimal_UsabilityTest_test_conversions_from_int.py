# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_conversions_from_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    self.assertEqual(Decimal(4).compare(3), Decimal(4).compare(Decimal(3)))
    self.assertEqual(Decimal(4).compare_signal(3), Decimal(4).compare_signal(Decimal(3)))
    self.assertEqual(Decimal(4).compare_total(3), Decimal(4).compare_total(Decimal(3)))
    self.assertEqual(Decimal(4).compare_total_mag(3), Decimal(4).compare_total_mag(Decimal(3)))
    self.assertEqual(Decimal(10101).logical_and(1001), Decimal(10101).logical_and(Decimal(1001)))
    self.assertEqual(Decimal(10101).logical_or(1001), Decimal(10101).logical_or(Decimal(1001)))
    self.assertEqual(Decimal(10101).logical_xor(1001), Decimal(10101).logical_xor(Decimal(1001)))
    self.assertEqual(Decimal(567).max(123), Decimal(567).max(Decimal(123)))
    self.assertEqual(Decimal(567).max_mag(123), Decimal(567).max_mag(Decimal(123)))
    self.assertEqual(Decimal(567).min(123), Decimal(567).min(Decimal(123)))
    self.assertEqual(Decimal(567).min_mag(123), Decimal(567).min_mag(Decimal(123)))
    self.assertEqual(Decimal(567).next_toward(123), Decimal(567).next_toward(Decimal(123)))
    self.assertEqual(Decimal(1234).quantize(100), Decimal(1234).quantize(Decimal(100)))
    self.assertEqual(Decimal(768).remainder_near(1234), Decimal(768).remainder_near(Decimal(1234)))
    self.assertEqual(Decimal(123).rotate(1), Decimal(123).rotate(Decimal(1)))
    self.assertEqual(Decimal(1234).same_quantum(1000), Decimal(1234).same_quantum(Decimal(1000)))
    self.assertEqual(Decimal('9.123').scaleb(-100), Decimal('9.123').scaleb(Decimal(-100)))
    self.assertEqual(Decimal(456).shift(-1), Decimal(456).shift(Decimal(-1)))
    self.assertEqual(Decimal(-12).fma(Decimal(45), 67), Decimal(-12).fma(Decimal(45), Decimal(67)))
    self.assertEqual(Decimal(-12).fma(45, 67), Decimal(-12).fma(Decimal(45), Decimal(67)))
    self.assertEqual(Decimal(-12).fma(45, Decimal(67)), Decimal(-12).fma(Decimal(45), Decimal(67)))
