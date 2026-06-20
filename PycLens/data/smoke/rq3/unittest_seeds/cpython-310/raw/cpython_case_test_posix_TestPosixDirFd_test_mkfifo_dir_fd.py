# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_mkfifo_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare() as (dir_fd, name, fullname):
        try:
            posix.mkfifo(name, stat.S_IRUSR | stat.S_IWUSR, dir_fd=dir_fd)
        except PermissionError as e:
            self.skipTest('posix.mkfifo(): %s' % e)
        self.addCleanup(posix.unlink, fullname)
        self.assertTrue(stat.S_ISFIFO(posix.stat(fullname).st_mode))
