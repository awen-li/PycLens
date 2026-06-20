# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_writev

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDWR | os.O_CREAT)
    try:
        n = os.writev(fd, (b'test1', b'tt2', b't3'))
        self.assertEqual(n, 10)
        os.lseek(fd, 0, os.SEEK_SET)
        self.assertEqual(b'test1tt2t3', posix.read(fd, 10))
        try:
            size = posix.writev(fd, [])
        except OSError:
            pass
        else:
            self.assertEqual(size, 0)
    finally:
        os.close(fd)
