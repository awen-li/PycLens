# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_zscore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    X = NormalDist(100, 15)
    self.assertEqual(X.zscore(142), 2.8)
    self.assertEqual(X.zscore(58), -2.8)
    self.assertEqual(X.zscore(100), 0.0)
    with self.assertRaises(TypeError):
        X.zscore()
    with self.assertRaises(TypeError):
        X.zscore(1, 1)
    with self.assertRaises(TypeError):
        X.zscore(None)
    with self.assertRaises(self.module.StatisticsError):
        NormalDist(1, 0).zscore(100)
