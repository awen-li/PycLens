# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_gammavariate_alpha_greater_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    random_mock.side_effect = [1e-08, 0.5, 0.3]
    returned_value = random.gammavariate(1.1, 2.3)
    self.assertAlmostEqual(returned_value, 2.53)
