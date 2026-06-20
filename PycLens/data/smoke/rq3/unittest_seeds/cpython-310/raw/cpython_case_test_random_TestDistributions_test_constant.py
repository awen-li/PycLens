# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_constant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = random.Random()
    N = 100
    for (variate, args, expected) in [(g.uniform, (10.0, 10.0), 10.0), (g.triangular, (10.0, 10.0), 10.0), (g.triangular, (10.0, 10.0, 10.0), 10.0), (g.expovariate, (float('inf'),), 0.0), (g.vonmisesvariate, (3.0, float('inf')), 3.0), (g.gauss, (10.0, 0.0), 10.0), (g.lognormvariate, (0.0, 0.0), 1.0), (g.lognormvariate, (-float('inf'), 0.0), 0.0), (g.normalvariate, (10.0, 0.0), 10.0), (g.paretovariate, (float('inf'),), 1.0), (g.weibullvariate, (10.0, float('inf')), 10.0), (g.weibullvariate, (0.0, 10.0), 0.0)]:
        for i in range(N):
            self.assertEqual(variate(*args), expected)
