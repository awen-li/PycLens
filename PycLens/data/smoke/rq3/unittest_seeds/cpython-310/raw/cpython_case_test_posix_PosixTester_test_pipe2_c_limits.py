# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_pipe2_c_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    self.assertRaises(OverflowError, os.pipe2, _testcapi.INT_MAX + 1)
    self.assertRaises(OverflowError, os.pipe2, _testcapi.UINT_MAX + 1)
