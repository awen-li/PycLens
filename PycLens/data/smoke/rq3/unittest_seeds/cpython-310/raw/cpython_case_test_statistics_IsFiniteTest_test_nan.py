# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: IsFiniteTest_test_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in (float('nan'), Decimal('NAN'), Decimal('sNAN')):
        self.assertFalse(statistics._isfinite(x))
