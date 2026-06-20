# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_precomputed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (func, data, elem, expected) in self.precomputedCases:
        self.assertEqual(func(data, elem), expected)
        self.assertEqual(func(UserList(data), elem), expected)
