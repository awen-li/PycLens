# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_gammavariate_alpha_between_zero_and_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _e = random._e
    _exp = random._exp
    _log = random._log
    alpha = 0.35
    beta = 1.45
    b = (_e + alpha) / _e
    epsilon = 0.01
    r1 = 0.8859296441566
    r2 = 0.3678794411714
    random_mock.side_effect = [r1, r2 + epsilon, r1, r2]
    returned_value = random.gammavariate(alpha, beta)
    self.assertAlmostEqual(returned_value, 1.4499999999997544)
    r1 = 0.8959296441566
    r2 = 0.9445400408898141
    random_mock.side_effect = [r1, r2 + epsilon, r1, r2]
    returned_value = random.gammavariate(alpha, beta)
    self.assertAlmostEqual(returned_value, 1.5830349561760781)
