# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_pwritev_overflow_32bits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_RDWR | os.O_CREAT)
    try:
        with self.assertRaises(OSError) as cm:
            os.pwritev(fd, [b'x' * 2 ** 16] * 2 ** 15, 0)
        self.assertEqual(cm.exception.errno, errno.EINVAL)
    finally:
        os.close(fd)
