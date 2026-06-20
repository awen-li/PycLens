# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_mod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        (1 + 1j) % (1 + 0j)
    with self.assertRaises(TypeError):
        (1 + 1j) % 1.0
    with self.assertRaises(TypeError):
        (1 + 1j) % 1
    with self.assertRaises(TypeError):
        1.0 % (1 + 0j)
    with self.assertRaises(TypeError):
        1 % (1 + 0j)
