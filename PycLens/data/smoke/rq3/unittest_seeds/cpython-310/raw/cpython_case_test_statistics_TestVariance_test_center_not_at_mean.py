# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestVariance_test_center_not_at_mean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = (1.0, 2.0)
    self.assertEqual(self.func(data), 0.5)
    self.assertEqual(self.func(data, xbar=2.0), 1.0)
