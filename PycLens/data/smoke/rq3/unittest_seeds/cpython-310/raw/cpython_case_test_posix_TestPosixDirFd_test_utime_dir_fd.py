# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixDirFd_test_utime_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.prepare_file() as (dir_fd, name, fullname):
        now = time.time()
        posix.utime(name, None, dir_fd=dir_fd)
        posix.utime(name, dir_fd=dir_fd)
        self.assertRaises(TypeError, posix.utime, name, now, dir_fd=dir_fd)
        self.assertRaises(TypeError, posix.utime, name, (None, None), dir_fd=dir_fd)
        self.assertRaises(TypeError, posix.utime, name, (now, None), dir_fd=dir_fd)
        self.assertRaises(TypeError, posix.utime, name, (None, now), dir_fd=dir_fd)
        self.assertRaises(TypeError, posix.utime, name, (now, 'x'), dir_fd=dir_fd)
        posix.utime(name, (int(now), int(now)), dir_fd=dir_fd)
        posix.utime(name, (now, now), dir_fd=dir_fd)
        posix.utime(name, (int(now), int((now - int(now)) * 1000000000.0)), dir_fd=dir_fd)
        posix.utime(name, dir_fd=dir_fd, times=(int(now), int((now - int(now)) * 1000000000.0)))
        if os.utime in os.supports_follow_symlinks:
            try:
                posix.utime(name, follow_symlinks=False, dir_fd=dir_fd)
            except ValueError:
                pass
