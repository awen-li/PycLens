# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_float_mod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = operator.mod
    self.assertEqualAndEqualSign(mod(-1.0, 1.0), 0.0)
    self.assertEqualAndEqualSign(mod(-1e-100, 1.0), 1.0)
    self.assertEqualAndEqualSign(mod(-0.0, 1.0), 0.0)
    self.assertEqualAndEqualSign(mod(0.0, 1.0), 0.0)
    self.assertEqualAndEqualSign(mod(1e-100, 1.0), 1e-100)
    self.assertEqualAndEqualSign(mod(1.0, 1.0), 0.0)
    self.assertEqualAndEqualSign(mod(-1.0, -1.0), -0.0)
    self.assertEqualAndEqualSign(mod(-1e-100, -1.0), -1e-100)
    self.assertEqualAndEqualSign(mod(-0.0, -1.0), -0.0)
    self.assertEqualAndEqualSign(mod(0.0, -1.0), -0.0)
    self.assertEqualAndEqualSign(mod(1e-100, -1.0), -1.0)
    self.assertEqualAndEqualSign(mod(1.0, -1.0), -0.0)
