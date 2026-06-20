# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_pread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDWR | os.O_CREAT)
    try:
        os.write(fd, b'test')
        os.lseek(fd, 0, os.SEEK_SET)
        self.assertEqual(b'es', posix.pread(fd, 2, 1))
        self.assertEqual(b'te', posix.read(fd, 2))
    finally:
        os.close(fd)
