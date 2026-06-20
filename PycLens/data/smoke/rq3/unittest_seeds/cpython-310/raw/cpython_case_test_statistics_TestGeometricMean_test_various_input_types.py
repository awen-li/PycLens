# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestGeometricMean_test_various_input_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    geometric_mean = statistics.geometric_mean
    D = Decimal
    F = Fraction
    expected_mean = 4.18886
    for (data, kind) in [([3.5, 4.0, 5.25], 'floats'), ([D('3.5'), D('4.0'), D('5.25')], 'decimals'), ([F(7, 2), F(4, 1), F(21, 4)], 'fractions'), ([3.5, 4, F(21, 4)], 'mixed types'), ((3.5, 4.0, 5.25), 'tuple'), (iter([3.5, 4.0, 5.25]), 'iterator')]:
        actual_mean = geometric_mean(data)
        self.assertIs(type(actual_mean), float, kind)
        self.assertAlmostEqual(actual_mean, expected_mean, places=5)
