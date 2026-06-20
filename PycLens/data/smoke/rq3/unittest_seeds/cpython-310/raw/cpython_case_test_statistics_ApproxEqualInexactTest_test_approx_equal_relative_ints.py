# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualInexactTest_test_approx_equal_relative_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(approx_equal(64, 47, tol=0, rel=0.36))
    self.assertTrue(approx_equal(64, 47, tol=0, rel=0.37))
    self.assertTrue(approx_equal(449, 512, tol=0, rel=0.125))
    self.assertTrue(approx_equal(448, 512, tol=0, rel=0.125))
    self.assertFalse(approx_equal(447, 512, tol=0, rel=0.125))
