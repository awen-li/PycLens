# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_path_with_null_byte

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fn = os.fsencode(os_helper.TESTFN)
    fn_with_NUL = fn + b'\x00'
    self.addCleanup(os_helper.unlink, fn)
    os_helper.unlink(fn)
    fd = None
    try:
        with self.assertRaises(ValueError):
            fd = os.open(fn_with_NUL, os.O_WRONLY | os.O_CREAT)
    finally:
        if fd is not None:
            os.close(fd)
    self.assertFalse(os.path.exists(fn))
    self.assertRaises(ValueError, os.mkdir, fn_with_NUL)
    self.assertFalse(os.path.exists(fn))
    open(fn, 'wb').close()
    self.assertRaises(ValueError, os.stat, fn_with_NUL)
