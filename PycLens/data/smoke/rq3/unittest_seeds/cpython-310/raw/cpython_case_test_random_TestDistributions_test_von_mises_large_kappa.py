# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_von_mises_large_kappa

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    random.vonmisesvariate(0, 1000000000000000.0)
    random.vonmisesvariate(0, 1e+100)
