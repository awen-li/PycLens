# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_zero_tolerance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zero_tolerance_close_examples = [(1.0, 1.0), (-3.4, -3.4), (-1e-300, -1e-300)]
    self.assertAllClose(zero_tolerance_close_examples, rel_tol=0.0)
    zero_tolerance_not_close_examples = [(1.0, 1.000000000000001), (0.99999999999999, 1.0), (1e+200, 9.99999999999999e+199)]
    self.assertAllNotClose(zero_tolerance_not_close_examples, rel_tol=0.0)
