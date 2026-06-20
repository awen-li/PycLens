# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PosixUidGidTests_test_setgid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.getuid() != 0 and (not HAVE_WHEEL_GROUP):
        self.assertRaises(OSError, os.setgid, 0)
    self.assertRaises(TypeError, os.setgid, 'not an int')
    self.assertRaises(OverflowError, os.setgid, self.GID_OVERFLOW)
