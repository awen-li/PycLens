# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_sample_distribution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 5
    pop = range(n)
    trials = 10000
    for k in range(n):
        expected = factorial(n) // factorial(n - k)
        perms = {}
        for i in range(trials):
            perms[tuple(self.gen.sample(pop, k))] = None
            if len(perms) == expected:
                break
        else:
            self.fail()
