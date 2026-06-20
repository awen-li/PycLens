# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestPStdev_test_compare_to_variance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [random.uniform(-17, 24) for _ in range(1000)]
    expected = math.sqrt(statistics.pvariance(data))
    self.assertEqual(self.func(data), expected)
