# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_readv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDWR | os.O_CREAT)
    try:
        os.write(fd, b'test1tt2t3')
        os.lseek(fd, 0, os.SEEK_SET)
        buf = [bytearray(i) for i in [5, 3, 2]]
        self.assertEqual(posix.readv(fd, buf), 10)
        self.assertEqual([b'test1', b'tt2', b't3'], [bytes(i) for i in buf])
        try:
            size = posix.readv(fd, [])
        except OSError:
            pass
        else:
            self.assertEqual(size, 0)
    finally:
        os.close(fd)
