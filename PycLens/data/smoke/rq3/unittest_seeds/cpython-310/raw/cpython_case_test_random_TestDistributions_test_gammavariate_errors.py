# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestDistributions_test_gammavariate_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, random.gammavariate, -1, 3)
    self.assertRaises(ValueError, random.gammavariate, 0, 2)
    self.assertRaises(ValueError, random.gammavariate, 2, 0)
    self.assertRaises(ValueError, random.gammavariate, 1, -3)
