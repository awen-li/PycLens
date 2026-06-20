# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_gammavariate_alpha_equal_one_equals_expovariate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    beta = 3.14
    random_mock.side_effect = [1e-08, 1e-08]
    gammavariate_returned_value = random.gammavariate(1.0, beta)
    expovariate_returned_value = random.expovariate(1.0 / beta)
    self.assertAlmostEqual(gammavariate_returned_value, expovariate_returned_value)
