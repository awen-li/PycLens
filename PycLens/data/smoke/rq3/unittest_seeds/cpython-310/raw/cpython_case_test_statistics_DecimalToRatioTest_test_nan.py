# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: DecimalToRatioTest_test_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for nan in (Decimal('NAN'), Decimal('sNAN')):
        (num, den) = statistics._exact_ratio(nan)
        self.assertTrue(_nan_equal(num, nan))
        self.assertIs(den, None)
