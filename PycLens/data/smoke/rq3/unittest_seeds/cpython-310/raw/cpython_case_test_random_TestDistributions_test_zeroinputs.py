# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_zeroinputs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = random.Random()
    x = [g.random() for i in range(50)] + [0.0] * 5
    g.random = x[:].pop
    g.uniform(1, 10)
    g.random = x[:].pop
    g.paretovariate(1.0)
    g.random = x[:].pop
    g.expovariate(1.0)
    g.random = x[:].pop
    g.weibullvariate(1.0, 1.0)
    g.random = x[:].pop
    g.vonmisesvariate(1.0, 1.0)
    g.random = x[:].pop
    g.normalvariate(0.0, 1.0)
    g.random = x[:].pop
    g.gauss(0.0, 1.0)
    g.random = x[:].pop
    g.lognormvariate(0.0, 1.0)
    g.random = x[:].pop
    g.vonmisesvariate(0.0, 1.0)
    g.random = x[:].pop
    g.gammavariate(0.01, 1.0)
    g.random = x[:].pop
    g.gammavariate(1.0, 1.0)
    g.random = x[:].pop
    g.gammavariate(200.0, 1.0)
    g.random = x[:].pop
    g.betavariate(3.0, 3.0)
    g.random = x[:].pop
    g.triangular(0.0, 1.0, 1.0 / 3.0)
