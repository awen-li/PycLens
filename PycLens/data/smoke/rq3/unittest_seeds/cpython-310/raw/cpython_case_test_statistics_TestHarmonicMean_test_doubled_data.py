# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_doubled_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [random.uniform(1, 5) for _ in range(1000)]
    expected = self.func(data)
    actual = self.func(data * 2)
    self.assertApproxEqual(actual, expected)
