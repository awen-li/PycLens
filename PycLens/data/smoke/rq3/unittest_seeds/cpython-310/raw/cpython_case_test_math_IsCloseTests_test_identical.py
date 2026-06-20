# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_identical

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    identical_examples = [(2.0, 2.0), (1e+199, 1e+199), (1.123e-300, 1.123e-300), (12345, 12345.0), (0.0, -0.0), (345678, 345678)]
    self.assertAllClose(identical_examples, rel_tol=0.0, abs_tol=0.0)
