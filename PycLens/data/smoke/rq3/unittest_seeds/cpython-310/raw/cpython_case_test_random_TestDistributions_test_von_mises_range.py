# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_von_mises_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = random.Random()
    N = 100
    for mu in (0.0, 0.1, 3.1, 6.2):
        for kappa in (0.0, 2.3, 500.0):
            for _ in range(N):
                sample = g.vonmisesvariate(mu, kappa)
                self.assertTrue(0 <= sample <= random.TWOPI, msg='vonmisesvariate({}, {}) produced a result {} out of range [0, 2*pi]'.format(mu, kappa, sample))
