# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_open_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare() as (dir_fd, name, fullname):
        with open(fullname, 'wb') as outfile:
            outfile.write(b'testline\n')
        self.addCleanup(posix.unlink, fullname)
        fd = posix.open(name, posix.O_RDONLY, dir_fd=dir_fd)
        try:
            res = posix.read(fd, 9)
            self.assertEqual(b'testline\n', res)
        finally:
            posix.close(fd)
