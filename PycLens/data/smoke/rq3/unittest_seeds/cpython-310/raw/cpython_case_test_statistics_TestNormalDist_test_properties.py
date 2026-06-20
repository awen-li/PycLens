# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_properties

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    X = self.module.NormalDist(100, 15)
    self.assertEqual(X.mean, 100)
    self.assertEqual(X.median, 100)
    self.assertEqual(X.mode, 100)
    self.assertEqual(X.stdev, 15)
    self.assertEqual(X.variance, 225)
