# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_relative_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for x in [-178.34, -0.1, 0.1, 1.0, 36.97, 2847.136, 9145.074]:
        self.do_approx_equal_rel_test(x, 0.02)
        self.do_approx_equal_rel_test(x, 0.0001)
