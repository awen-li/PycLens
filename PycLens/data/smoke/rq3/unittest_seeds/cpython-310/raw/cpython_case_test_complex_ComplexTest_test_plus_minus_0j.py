# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_plus_minus_0j

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (z1, z2) = (0j, -0j)
    self.assertEqual(atan2(z1.imag, -1.0), atan2(0.0, -1.0))
    self.assertEqual(atan2(z2.imag, -1.0), atan2(-0.0, -1.0))
