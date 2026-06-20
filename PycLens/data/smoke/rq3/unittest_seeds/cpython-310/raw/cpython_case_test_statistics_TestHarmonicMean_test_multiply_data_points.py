# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_multiply_data_points

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = 111
    data = [3.4, 4.5, 4.9, 6.7, 6.8, 7.2, 8.0, 8.1, 9.4]
    expected = self.func(data) * c
    result = self.func([x * c for x in data])
    self.assertEqual(result, expected)
