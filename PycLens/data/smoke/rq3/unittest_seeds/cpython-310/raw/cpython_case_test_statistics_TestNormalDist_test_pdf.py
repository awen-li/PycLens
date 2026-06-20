# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_pdf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    X = NormalDist(100, 15)
    self.assertLess(X.pdf(99), X.pdf(100))
    self.assertLess(X.pdf(101), X.pdf(100))
    for i in range(50):
        self.assertAlmostEqual(X.pdf(100 - i), X.pdf(100 + i))
    dx = 2.0 ** (-10)
    for x in range(90, 111):
        est_pdf = (X.cdf(x + dx) - X.cdf(x)) / dx
        self.assertAlmostEqual(X.pdf(x), est_pdf, places=4)
    Z = NormalDist()
    for (x, px) in enumerate([0.3989, 0.3989, 0.3989, 0.3988, 0.3986, 0.3984, 0.3982, 0.398, 0.3977, 0.3973, 0.397, 0.3965, 0.3961, 0.3956, 0.3951, 0.3945, 0.3939, 0.3932, 0.3925, 0.3918, 0.391, 0.3902, 0.3894, 0.3885, 0.3876, 0.3867, 0.3857, 0.3847, 0.3836, 0.3825, 0.3814, 0.3802, 0.379, 0.3778, 0.3765, 0.3752, 0.3739, 0.3725, 0.3712, 0.3697, 0.3683, 0.3668, 0.3653, 0.3637, 0.3621, 0.3605, 0.3589, 0.3572, 0.3555, 0.3538]):
        self.assertAlmostEqual(Z.pdf(x / 100.0), px, places=4)
        self.assertAlmostEqual(Z.pdf(-x / 100.0), px, places=4)
    Y = NormalDist(100, 0)
    with self.assertRaises(self.module.StatisticsError):
        Y.pdf(90)
    self.assertEqual(X.pdf(float('-Inf')), 0.0)
    self.assertEqual(X.pdf(float('Inf')), 0.0)
    self.assertTrue(math.isnan(X.pdf(float('NaN'))))
