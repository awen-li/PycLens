# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: IsCloseTests_test_reject_complex_tolerances

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        self.isclose(1j, 1j, rel_tol=1j)
    with self.assertRaises(TypeError):
        self.isclose(1j, 1j, abs_tol=1j)
    with self.assertRaises(TypeError):
        self.isclose(1j, 1j, rel_tol=1j, abs_tol=1j)
