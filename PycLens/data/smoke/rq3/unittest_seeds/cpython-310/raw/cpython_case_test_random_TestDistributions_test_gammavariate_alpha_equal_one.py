# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_gammavariate_alpha_equal_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    random_mock.side_effect = [0.45]
    returned_value = random.gammavariate(1.0, 3.14)
    self.assertAlmostEqual(returned_value, 1.877208182372648)
