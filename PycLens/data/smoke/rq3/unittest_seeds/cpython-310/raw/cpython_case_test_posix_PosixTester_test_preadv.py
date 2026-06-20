# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_preadv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDWR | os.O_CREAT)
    try:
        os.write(fd, b'test1tt2t3t5t6t6t8')
        buf = [bytearray(i) for i in [5, 3, 2]]
        self.assertEqual(posix.preadv(fd, buf, 3), 10)
        self.assertEqual([b't1tt2', b't3t', b'5t'], list(buf))
    finally:
        os.close(fd)
