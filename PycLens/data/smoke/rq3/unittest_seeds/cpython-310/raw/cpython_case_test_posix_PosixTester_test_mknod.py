# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_mknod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os_helper.unlink(os_helper.TESTFN)
    mode = stat.S_IFIFO | stat.S_IRUSR | stat.S_IWUSR
    try:
        posix.mknod(os_helper.TESTFN, mode, 0)
    except OSError as e:
        self.assertIn(e.errno, (errno.EPERM, errno.EINVAL, errno.EACCES))
    else:
        self.assertTrue(stat.S_ISFIFO(posix.stat(os_helper.TESTFN).st_mode))
    os_helper.unlink(os_helper.TESTFN)
    try:
        posix.mknod(path=os_helper.TESTFN, mode=mode, device=0, dir_fd=None)
    except OSError as e:
        self.assertIn(e.errno, (errno.EPERM, errno.EINVAL, errno.EACCES))
