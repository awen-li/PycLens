# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestErrorHandling_test_arg_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in (self.module.bisect_left, self.module.bisect_right, self.module.insort_left, self.module.insort_right):
        self.assertRaises(TypeError, f, 10)
