# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_large_pyrange

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = self.module
    n = sys.maxsize
    data = Range(0, n - 1)
    self.assertEqual(mod.bisect_left(data, n - 3), n - 3)
    self.assertEqual(mod.bisect_right(data, n - 3), n - 2)
    self.assertEqual(mod.bisect_left(data, n - 3, n - 10, n), n - 3)
    self.assertEqual(mod.bisect_right(data, n - 3, n - 10, n), n - 2)
    x = n - 100
    mod.insort_left(data, x, x - 50, x + 50)
    self.assertEqual(data.last_insert, (x, x))
    x = n - 200
    mod.insort_right(data, x, x - 50, x + 50)
    self.assertEqual(data.last_insert, (x + 1, x))
