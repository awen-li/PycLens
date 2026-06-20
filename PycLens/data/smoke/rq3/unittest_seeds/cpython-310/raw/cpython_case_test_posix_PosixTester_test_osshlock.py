# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_osshlock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd1 = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_SHLOCK | os.O_CREAT)
    fd2 = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_SHLOCK | os.O_CREAT)
    os.close(fd2)
    os.close(fd1)
    if hasattr(posix, 'O_EXLOCK'):
        fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_SHLOCK | os.O_CREAT)
        self.assertRaises(OSError, os.open, os_helper.TESTFN, os.O_RDONLY | os.O_EXLOCK | os.O_NONBLOCK)
        os.close(fd)
