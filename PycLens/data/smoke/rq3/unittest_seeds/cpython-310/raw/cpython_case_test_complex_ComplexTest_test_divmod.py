# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_divmod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, divmod, 1 + 1j, 1 + 0j)
    self.assertRaises(TypeError, divmod, 1 + 1j, 1.0)
    self.assertRaises(TypeError, divmod, 1 + 1j, 1)
    self.assertRaises(TypeError, divmod, 1.0, 1 + 0j)
    self.assertRaises(TypeError, divmod, 1, 1 + 0j)
