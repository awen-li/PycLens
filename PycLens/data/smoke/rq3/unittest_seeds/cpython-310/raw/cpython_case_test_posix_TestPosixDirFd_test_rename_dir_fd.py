# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_rename_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare_file() as (dir_fd, name, fullname), self.prepare() as (dir_fd2, name2, fullname2):
        posix.rename(name, name2, src_dir_fd=dir_fd, dst_dir_fd=dir_fd2)
        posix.stat(fullname2)
        posix.rename(fullname2, fullname)
