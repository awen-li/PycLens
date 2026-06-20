# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: IsCloseTests_test_complex_near_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    near_zero_examples = [(0.001j, 0), (0.001, 0), (0.001 + 0.001j, 0), (-0.001 + 0.001j, 0), (0.001 - 0.001j, 0), (-0.001 - 0.001j, 0)]
    self.assertAllClose(near_zero_examples, abs_tol=0.0015)
    self.assertAllNotClose(near_zero_examples, abs_tol=0.0005)
    self.assertIsClose(0.001 - 0.001j, 0.001 + 0.001j, abs_tol=0.002)
    self.assertIsNotClose(0.001 - 0.001j, 0.001 + 0.001j, abs_tol=0.001)
