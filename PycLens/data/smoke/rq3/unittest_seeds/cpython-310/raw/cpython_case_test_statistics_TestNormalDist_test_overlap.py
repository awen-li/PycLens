# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestNormalDist_test_overlap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NormalDist = self.module.NormalDist
    for (X1, X2, published_result) in [(NormalDist(0.0, 2.0), NormalDist(1.0, 2.0), 0.80258), (NormalDist(0.0, 1.0), NormalDist(1.0, 2.0), 0.60993)]:
        self.assertAlmostEqual(X1.overlap(X2), published_result, places=4)
        self.assertAlmostEqual(X2.overlap(X1), published_result, places=4)

    def overlap_numeric(X, Y, *, steps=8192, z=5):
        """Numerical integration cross-check for overlap() """
        fsum = math.fsum
        center = (X.mean + Y.mean) / 2.0
        width = z * max(X.stdev, Y.stdev)
        start = center - width
        dx = 2.0 * width / steps
        x_arr = [start + i * dx for i in range(steps)]
        xp = list(map(X.pdf, x_arr))
        yp = list(map(Y.pdf, x_arr))
        total = max(fsum(xp), fsum(yp))
        return fsum(map(min, xp, yp)) / total
    for (X1, X2) in [(NormalDist(0.0, 2.0), NormalDist(1.0, 2.0)), (NormalDist(0.0, 1.0), NormalDist(1.0, 2.0)), (NormalDist(0.0, 1.0), NormalDist(1.0, 2.0)), (NormalDist(70, 4), NormalDist(65, 3.5)), (NormalDist(100, 15), NormalDist(110, 15)), (NormalDist(-100, 15), NormalDist(110, 15)), (NormalDist(-100, 15), NormalDist(-110, 15)), (NormalDist(100, 12), NormalDist(100, 15)), (NormalDist(100, 12), NormalDist(110, 15)), (NormalDist(100, 12), NormalDist(150, 15)), (NormalDist(100, 12), NormalDist(150, 35)), (NormalDist(1.0, 0.002), NormalDist(1.001, 0.003)), (NormalDist(1.0, 0.002), NormalDist(1.006, 0.0003)), (NormalDist(1.0, 0.002), NormalDist(1.001, 0.099))]:
        self.assertAlmostEqual(X1.overlap(X2), overlap_numeric(X1, X2), places=5)
        self.assertAlmostEqual(X2.overlap(X1), overlap_numeric(X1, X2), places=5)
    X = NormalDist()
    with self.assertRaises(TypeError):
        X.overlap()
    with self.assertRaises(TypeError):
        X.overlap(X, X)
    with self.assertRaises(TypeError):
        X.overlap(None)
    with self.assertRaises(self.module.StatisticsError):
        X.overlap(NormalDist(1, 0))
    with self.assertRaises(self.module.StatisticsError):
        NormalDist(1, 0).overlap(X)
