# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e_expected = 2.718281828459045
    pi_expected = 3.141592653589793
    self.assertAlmostEqual(cmath.pi, pi_expected, places=9, msg='cmath.pi is {}; should be {}'.format(cmath.pi, pi_expected))
    self.assertAlmostEqual(cmath.e, e_expected, places=9, msg='cmath.e is {}; should be {}'.format(cmath.e, e_expected))
