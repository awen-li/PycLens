# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_inv_cdf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    iq = NormalDist(100, 15)
    self.assertEqual(iq.inv_cdf(0.5), iq.mean)
    Z = NormalDist()
    pp = {5.0: (0.0, 1.645, 2.576, 3.291, 3.891, 4.417, 4.892, 5.327, 5.731, 6.109), 2.5: (0.674, 1.96, 2.807, 3.481, 4.056, 4.565, 5.026, 5.451, 5.847, 6.219), 1.0: (1.282, 2.326, 3.09, 3.719, 4.265, 4.753, 5.199, 5.612, 5.998, 6.361)}
    for (base, row) in pp.items():
        for (exp, x) in enumerate(row, start=1):
            p = base * 10.0 ** (-exp)
            self.assertAlmostEqual(-Z.inv_cdf(p), x, places=3)
            p = 1.0 - p
            self.assertAlmostEqual(Z.inv_cdf(p), x, places=3)
    self.assertAlmostEqual(NormalDist(40, 1.5).inv_cdf(0.908789), 42.000002)
    n = 2 ** 20
    for p in range(1, n):
        p /= n
        self.assertAlmostEqual(iq.cdf(iq.inv_cdf(p)), p)
    for e in range(1, 51):
        p = 2.0 ** (-e)
        self.assertAlmostEqual(iq.cdf(iq.inv_cdf(p)), p)
        p = 1.0 - p
        self.assertAlmostEqual(iq.cdf(iq.inv_cdf(p)), p)
    for x in range(200):
        self.assertAlmostEqual(iq.inv_cdf(iq.cdf(x)), x, places=5)
    with self.assertRaises(self.module.StatisticsError):
        iq.inv_cdf(0.0)
    with self.assertRaises(self.module.StatisticsError):
        iq.inv_cdf(-0.1)
    with self.assertRaises(self.module.StatisticsError):
        iq.inv_cdf(1.0)
    with self.assertRaises(self.module.StatisticsError):
        iq.inv_cdf(1.1)
    with self.assertRaises(self.module.StatisticsError):
        iq = NormalDist(100, 0)
        iq.inv_cdf(0.5)
    self.assertTrue(math.isnan(Z.inv_cdf(float('NaN'))))
