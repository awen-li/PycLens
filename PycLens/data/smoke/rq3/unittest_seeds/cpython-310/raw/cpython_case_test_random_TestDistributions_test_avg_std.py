# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_avg_std

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = random.Random()
    N = 5000
    x = [i / float(N) for i in range(1, N)]
    for (variate, args, mu, sigmasqrd) in [(g.uniform, (1.0, 10.0), (10.0 + 1.0) / 2, (10.0 - 1.0) ** 2 / 12), (g.triangular, (0.0, 1.0, 1.0 / 3.0), 4.0 / 9.0, 7.0 / 9.0 / 18.0), (g.expovariate, (1.5,), 1 / 1.5, 1 / 1.5 ** 2), (g.vonmisesvariate, (1.23, 0), pi, pi ** 2 / 3), (g.paretovariate, (5.0,), 5.0 / (5.0 - 1), 5.0 / ((5.0 - 1) ** 2 * (5.0 - 2))), (g.weibullvariate, (1.0, 3.0), gamma(1 + 1 / 3.0), gamma(1 + 2 / 3.0) - gamma(1 + 1 / 3.0) ** 2)]:
        g.random = x[:].pop
        y = []
        for i in range(len(x)):
            try:
                y.append(variate(*args))
            except IndexError:
                pass
        s1 = s2 = 0
        for e in y:
            s1 += e
            s2 += (e - mu) ** 2
        N = len(y)
        self.assertAlmostEqual(s1 / N, mu, places=2, msg='%s%r' % (variate.__name__, args))
        self.assertAlmostEqual(s2 / (N - 1), sigmasqrd, places=2, msg='%s%r' % (variate.__name__, args))
