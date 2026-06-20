# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_cdf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    X = NormalDist(100, 15)
    cdfs = [X.cdf(x) for x in range(1, 200)]
    self.assertEqual(set(map(type, cdfs)), {float})
    self.assertEqual(cdfs, sorted(cdfs))
    self.assertEqual(X.cdf(100), 0.5)
    Z = NormalDist()
    for (z, cum_prob) in [(0.0, 0.5), (0.01, 0.50399), (0.02, 0.50798), (0.14, 0.55567), (0.29, 0.61409), (0.33, 0.6293), (0.54, 0.7054), (0.6, 0.72575), (1.17, 0.879), (1.6, 0.9452), (2.05, 0.97982), (2.89, 0.99807), (3.52, 0.99978), (3.98, 0.99997), (4.07, 0.99998)]:
        self.assertAlmostEqual(Z.cdf(z), cum_prob, places=5)
        self.assertAlmostEqual(Z.cdf(-z), 1.0 - cum_prob, places=5)
    Y = NormalDist(100, 0)
    with self.assertRaises(self.module.StatisticsError):
        Y.cdf(90)
    self.assertEqual(X.cdf(float('-Inf')), 0.0)
    self.assertEqual(X.cdf(float('Inf')), 1.0)
    self.assertTrue(math.isnan(X.cdf(float('NaN'))))
