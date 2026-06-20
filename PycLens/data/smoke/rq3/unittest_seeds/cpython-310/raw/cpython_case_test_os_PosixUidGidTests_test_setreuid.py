# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PosixUidGidTests_test_setreuid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.getuid() != 0:
        self.assertRaises(OSError, os.setreuid, 0, 0)
    self.assertRaises(TypeError, os.setreuid, 'not an int', 0)
    self.assertRaises(TypeError, os.setreuid, 0, 'not an int')
    self.assertRaises(OverflowError, os.setreuid, self.UID_OVERFLOW, 0)
    self.assertRaises(OverflowError, os.setreuid, 0, self.UID_OVERFLOW)
