# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ApproxEqualSpecialsTest_test_float_zeroes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nzero = math.copysign(0.0, -1)
    self.assertTrue(approx_equal(nzero, 0.0, tol=0.1, rel=0.1))
