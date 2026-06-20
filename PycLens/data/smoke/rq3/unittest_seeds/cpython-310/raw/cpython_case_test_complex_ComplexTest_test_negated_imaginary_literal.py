# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_negated_imaginary_literal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    z0 = -0j
    z1 = -7j
    z2 = -1e309j
    self.assertFloatsAreIdentical(z0.real, -0.0)
    self.assertFloatsAreIdentical(z0.imag, -0.0)
    self.assertFloatsAreIdentical(z1.real, -0.0)
    self.assertFloatsAreIdentical(z1.imag, -7.0)
    self.assertFloatsAreIdentical(z2.real, -0.0)
    self.assertFloatsAreIdentical(z2.imag, -INF)
