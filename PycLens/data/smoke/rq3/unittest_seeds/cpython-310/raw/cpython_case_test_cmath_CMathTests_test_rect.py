# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_rect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertCEqual(rect(0, 0), (0, 0))
    self.assertCEqual(rect(1, 0), (1.0, 0))
    self.assertCEqual(rect(1, -pi), (-1.0, 0))
    self.assertCEqual(rect(1, pi / 2), (0, 1.0))
    self.assertCEqual(rect(1, -pi / 2), (0, -1.0))
