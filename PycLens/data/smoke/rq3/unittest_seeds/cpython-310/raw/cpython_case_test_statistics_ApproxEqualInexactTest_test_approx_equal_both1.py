# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_both1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.do_check_both(7.955, 7.952, 0.004, 0.00038, True, True)
    self.do_check_both(-7.387, -7.386, 0.002, 0.0002, True, True)
