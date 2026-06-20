# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_fstatvfs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = open(os_helper.TESTFN)
    try:
        self.assertTrue(posix.fstatvfs(fp.fileno()))
        self.assertTrue(posix.statvfs(fp.fileno()))
    finally:
        fp.close()
