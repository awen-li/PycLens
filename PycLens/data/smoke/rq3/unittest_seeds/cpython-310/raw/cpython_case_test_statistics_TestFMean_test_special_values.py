# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestFMean_test_special_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmean = statistics.fmean
    NaN = float('Nan')
    Inf = float('Inf')
    self.assertTrue(math.isnan(fmean([10, NaN])), 'nan')
    self.assertTrue(math.isnan(fmean([NaN, Inf])), 'nan and infinity')
    self.assertTrue(math.isinf(fmean([10, Inf])), 'infinity')
    with self.assertRaises(ValueError):
        fmean([Inf, -Inf])
