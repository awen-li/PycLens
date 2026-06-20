# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PosixUidGidTests_test_seteuid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.getuid() != 0:
        self.assertRaises(OSError, os.seteuid, 0)
    self.assertRaises(TypeError, os.setegid, 'not an int')
    self.assertRaises(OverflowError, os.seteuid, self.UID_OVERFLOW)
