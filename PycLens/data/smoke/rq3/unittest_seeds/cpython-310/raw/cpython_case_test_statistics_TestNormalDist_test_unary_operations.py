# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_unary_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    X = NormalDist(100, 12)
    Y = +X
    self.assertIsNot(X, Y)
    self.assertEqual(X.mean, Y.mean)
    self.assertEqual(X.stdev, Y.stdev)
    Y = -X
    self.assertIsNot(X, Y)
    self.assertEqual(X.mean, -Y.mean)
    self.assertEqual(X.stdev, Y.stdev)
