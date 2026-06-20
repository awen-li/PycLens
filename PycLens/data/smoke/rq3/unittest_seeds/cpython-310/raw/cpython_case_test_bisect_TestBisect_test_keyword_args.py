# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_keyword_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [10, 20, 30, 40, 50]
    self.assertEqual(self.module.bisect_left(a=data, x=25, lo=1, hi=3), 2)
    self.assertEqual(self.module.bisect_right(a=data, x=25, lo=1, hi=3), 2)
    self.assertEqual(self.module.bisect(a=data, x=25, lo=1, hi=3), 2)
    self.module.insort_left(a=data, x=25, lo=1, hi=3)
    self.module.insort_right(a=data, x=25, lo=1, hi=3)
    self.module.insort(a=data, x=25, lo=1, hi=3)
    self.assertEqual(data, [10, 20, 25, 25, 25, 30, 40, 50])
