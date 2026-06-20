# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_pwritev_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDWR | os.O_CREAT)
    try:
        os.write(fd, b'xx')
        os.lseek(fd, 0, os.SEEK_SET)
        n = os.pwritev(fd, [b'test1', b'tt2', b't3'], 2, os.RWF_SYNC)
        self.assertEqual(n, 10)
        os.lseek(fd, 0, os.SEEK_SET)
        self.assertEqual(b'xxtest1tt2', posix.read(fd, 100))
    finally:
        os.close(fd)
