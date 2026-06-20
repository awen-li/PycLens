# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_utime_with_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    now = time.time()
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    try:
        posix.utime(fd)
        posix.utime(fd, None)
        self.assertRaises(TypeError, posix.utime, fd, (None, None))
        self.assertRaises(TypeError, posix.utime, fd, (now, None))
        self.assertRaises(TypeError, posix.utime, fd, (None, now))
        posix.utime(fd, (int(now), int(now)))
        posix.utime(fd, (now, now))
        self.assertRaises(ValueError, posix.utime, fd, (now, now), ns=(now, now))
        self.assertRaises(ValueError, posix.utime, fd, (now, 0), ns=(None, None))
        self.assertRaises(ValueError, posix.utime, fd, (None, None), ns=(now, 0))
        posix.utime(fd, (int(now), int((now - int(now)) * 1000000000.0)))
        posix.utime(fd, ns=(int(now), int((now - int(now)) * 1000000000.0)))
    finally:
        os.close(fd)
