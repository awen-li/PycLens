# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: IsCloseTests_test_identical_infinite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsClose(INF, INF)
    self.assertIsClose(INF, INF, abs_tol=0.0)
    self.assertIsClose(NINF, NINF)
    self.assertIsClose(NINF, NINF, abs_tol=0.0)
