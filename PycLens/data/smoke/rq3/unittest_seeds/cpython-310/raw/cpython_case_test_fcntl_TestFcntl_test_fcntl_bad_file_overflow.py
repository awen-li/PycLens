# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_fcntl_bad_file_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import INT_MAX, INT_MIN
    with self.assertRaises(OverflowError):
        fcntl.fcntl(INT_MAX + 1, fcntl.F_SETFL, os.O_NONBLOCK)
    with self.assertRaises(OverflowError):
        fcntl.fcntl(BadFile(INT_MAX + 1), fcntl.F_SETFL, os.O_NONBLOCK)
    with self.assertRaises(OverflowError):
        fcntl.fcntl(INT_MIN - 1, fcntl.F_SETFL, os.O_NONBLOCK)
    with self.assertRaises(OverflowError):
        fcntl.fcntl(BadFile(INT_MIN - 1), fcntl.F_SETFL, os.O_NONBLOCK)
