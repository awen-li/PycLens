# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestVariance_test_accuracy_bug_20499

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [0, 0, 2]
    exact = 4 / 3
    result = self.func(data)
    self.assertEqual(result, exact)
    self.assertIsInstance(result, float)
