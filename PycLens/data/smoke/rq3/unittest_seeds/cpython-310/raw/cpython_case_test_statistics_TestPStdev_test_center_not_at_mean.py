# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestPStdev_test_center_not_at_mean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = (3, 6, 7, 10)
    self.assertEqual(self.func(data), 2.5)
    self.assertEqual(self.func(data, mu=0.5), 6.5)
