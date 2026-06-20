# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestPVariance_test_accuracy_bug_20499

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [0, 0, 1]
    exact = 2 / 9
    result = self.func(data)
    self.assertEqual(result, exact)
    self.assertIsInstance(result, float)
