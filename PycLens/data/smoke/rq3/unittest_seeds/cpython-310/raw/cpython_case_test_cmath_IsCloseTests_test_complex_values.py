# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: IsCloseTests_test_complex_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    complex_examples = [(1.0 + 1j, 1.000000000001 + 1j), (1.0 + 1j, 1.0 + 1.000000000001j), (-1.0 + 1j, -1.000000000001 + 1j), (1.0 - 1j, 1.0 - 0.999999999999j)]
    self.assertAllClose(complex_examples, rel_tol=1e-12)
    self.assertAllNotClose(complex_examples, rel_tol=1e-13)
