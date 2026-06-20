# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_near_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    near_zero_examples = [(1e-09, 0.0), (-1e-09, 0.0), (-1e-150, 0.0)]
    self.assertAllNotClose(near_zero_examples, rel_tol=0.9)
    self.assertAllClose(near_zero_examples, abs_tol=1e-08)
