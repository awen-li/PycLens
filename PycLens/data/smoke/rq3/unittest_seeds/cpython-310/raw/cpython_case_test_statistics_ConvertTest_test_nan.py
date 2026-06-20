# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ConvertTest_test_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for nan in (float('nan'), Decimal('NAN'), Decimal('sNAN')):
        x = statistics._convert(nan, type(nan))
        self.assertTrue(_nan_equal(x, nan))
