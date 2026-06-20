# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: DecimalToRatioTest_test_sign

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    numbers = [Decimal('9.8765e12'), Decimal('9.8765e-12')]
    for d in numbers:
        assert d > 0
        (num, den) = statistics._exact_ratio(d)
        self.assertGreaterEqual(num, 0)
        self.assertGreater(den, 0)
        (num, den) = statistics._exact_ratio(-d)
        self.assertLessEqual(num, 0)
        self.assertGreater(den, 0)
