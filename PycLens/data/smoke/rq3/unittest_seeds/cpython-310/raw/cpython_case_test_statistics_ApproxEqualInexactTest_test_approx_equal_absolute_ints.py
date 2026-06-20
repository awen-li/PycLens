# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_absolute_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in [-10737, -1975, -7, -2, 0, 1, 9, 37, 423, 9874, 23789110]:
        self.do_approx_equal_abs_test(n, 10)
        self.do_approx_equal_abs_test(n, 2)
