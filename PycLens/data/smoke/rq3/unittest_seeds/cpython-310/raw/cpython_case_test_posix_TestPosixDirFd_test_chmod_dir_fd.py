# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_chmod_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare_file() as (dir_fd, name, fullname):
        posix.chmod(fullname, stat.S_IRUSR)
        posix.chmod(name, stat.S_IRUSR | stat.S_IWUSR, dir_fd=dir_fd)
        s = posix.stat(fullname)
        self.assertEqual(s.st_mode & stat.S_IRWXU, stat.S_IRUSR | stat.S_IWUSR)
