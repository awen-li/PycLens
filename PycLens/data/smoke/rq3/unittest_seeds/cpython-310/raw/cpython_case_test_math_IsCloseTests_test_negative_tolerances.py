# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_negative_tolerances

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        self.assertIsClose(1, 1, rel_tol=-1e-100)
    with self.assertRaises(ValueError):
        self.assertIsClose(1, 1, rel_tol=1e-100, abs_tol=-10000000000.0)
