# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_readlink_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare() as (dir_fd, name, fullname):
        os.symlink('symlink', fullname)
        self.addCleanup(posix.unlink, fullname)
        self.assertEqual(posix.readlink(name, dir_fd=dir_fd), 'symlink')
