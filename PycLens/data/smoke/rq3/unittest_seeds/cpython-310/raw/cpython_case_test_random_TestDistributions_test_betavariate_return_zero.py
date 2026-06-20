# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_betavariate_return_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gammavariate_mock.return_value = 0.0
    self.assertEqual(0.0, random.betavariate(2.71828, 3.14159))
