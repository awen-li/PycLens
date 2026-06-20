# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_osexlock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_EXLOCK | os.O_CREAT)
    self.assertRaises(OSError, os.open, os_helper.TESTFN, os.O_WRONLY | os.O_EXLOCK | os.O_NONBLOCK)
    os.close(fd)
    if hasattr(posix, 'O_SHLOCK'):
        fd = os.open(os_helper.TESTFN, os.O_WRONLY | os.O_SHLOCK | os.O_CREAT)
        self.assertRaises(OSError, os.open, os_helper.TESTFN, os.O_WRONLY | os.O_EXLOCK | os.O_NONBLOCK)
        os.close(fd)
