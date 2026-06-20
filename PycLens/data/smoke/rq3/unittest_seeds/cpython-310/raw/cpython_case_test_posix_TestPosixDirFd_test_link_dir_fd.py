# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_link_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare_file() as (dir_fd, name, fullname), self.prepare() as (dir_fd2, linkname, fulllinkname):
        try:
            posix.link(name, linkname, src_dir_fd=dir_fd, dst_dir_fd=dir_fd2)
        except PermissionError as e:
            self.skipTest('posix.link(): %s' % e)
        self.addCleanup(posix.unlink, fulllinkname)
        self.assertEqual(posix.stat(fullname)[1], posix.stat(fulllinkname)[1])
