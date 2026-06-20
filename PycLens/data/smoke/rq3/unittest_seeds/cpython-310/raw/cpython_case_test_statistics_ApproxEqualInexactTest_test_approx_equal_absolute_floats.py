# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_absolute_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [-284.126, -97.1, -3.4, -2.15, 0.5, 1.0, 7.8, 4.23, 3817.4]:
        self.do_approx_equal_abs_test(x, 1.5)
        self.do_approx_equal_abs_test(x, 0.01)
        self.do_approx_equal_abs_test(x, 0.0001)
