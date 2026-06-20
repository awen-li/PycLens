# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_flock_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    self.assertRaises(OverflowError, fcntl.flock, _testcapi.INT_MAX + 1, fcntl.LOCK_SH)
