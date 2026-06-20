# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_symlink_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare() as (dir_fd, name, fullname):
        posix.symlink('symlink', name, dir_fd=dir_fd)
        self.addCleanup(posix.unlink, fullname)
        self.assertEqual(posix.readlink(fullname), 'symlink')
