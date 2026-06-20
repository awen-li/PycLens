# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_utime_nofollow_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    now = time.time()
    posix.utime(os_helper.TESTFN, None, follow_symlinks=False)
    self.assertRaises(TypeError, posix.utime, os_helper.TESTFN, (None, None), follow_symlinks=False)
    self.assertRaises(TypeError, posix.utime, os_helper.TESTFN, (now, None), follow_symlinks=False)
    self.assertRaises(TypeError, posix.utime, os_helper.TESTFN, (None, now), follow_symlinks=False)
    posix.utime(os_helper.TESTFN, (int(now), int(now)), follow_symlinks=False)
    posix.utime(os_helper.TESTFN, (now, now), follow_symlinks=False)
    posix.utime(os_helper.TESTFN, follow_symlinks=False)
