# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_both4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.do_check_both(2.78, 2.75, 0.01, 0.001, False, False)
    self.do_check_both(971.44, 971.47, 0.02, 3e-05, False, False)
