# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_mknod_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare() as (dir_fd, name, fullname):
        mode = stat.S_IFIFO | stat.S_IRUSR | stat.S_IWUSR
        try:
            posix.mknod(name, mode, 0, dir_fd=dir_fd)
        except OSError as e:
            self.assertIn(e.errno, (errno.EPERM, errno.EINVAL, errno.EACCES))
        else:
            self.addCleanup(posix.unlink, fullname)
            self.assertTrue(stat.S_ISFIFO(posix.stat(fullname).st_mode))
