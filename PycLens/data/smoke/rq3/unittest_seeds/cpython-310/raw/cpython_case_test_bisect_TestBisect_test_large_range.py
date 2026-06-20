# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_large_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = self.module
    n = sys.maxsize
    data = range(n - 1)
    self.assertEqual(mod.bisect_left(data, n - 3), n - 3)
    self.assertEqual(mod.bisect_right(data, n - 3), n - 2)
    self.assertEqual(mod.bisect_left(data, n - 3, n - 10, n), n - 3)
    self.assertEqual(mod.bisect_right(data, n - 3, n - 10, n), n - 2)
