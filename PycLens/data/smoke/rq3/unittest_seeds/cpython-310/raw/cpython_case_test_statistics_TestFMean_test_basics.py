# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestFMean_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmean = statistics.fmean
    D = Decimal
    F = Fraction
    for (data, expected_mean, kind) in [([3.5, 4.0, 5.25], 4.25, 'floats'), ([D('3.5'), D('4.0'), D('5.25')], 4.25, 'decimals'), ([F(7, 2), F(4, 1), F(21, 4)], 4.25, 'fractions'), ([True, False, True, True, False], 0.6, 'booleans'), ([3.5, 4, F(21, 4)], 4.25, 'mixed types'), ((3.5, 4.0, 5.25), 4.25, 'tuple'), (iter([3.5, 4.0, 5.25]), 4.25, 'iterator')]:
        actual_mean = fmean(data)
        self.assertIs(type(actual_mean), float, kind)
        self.assertEqual(actual_mean, expected_mean, kind)
