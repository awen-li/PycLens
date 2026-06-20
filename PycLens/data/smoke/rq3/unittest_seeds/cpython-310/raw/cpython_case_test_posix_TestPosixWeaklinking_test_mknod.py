# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_mknod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_MKNODAT')
    if self.mac_ver >= (13, 0):
        self.assertIn('HAVE_MKNODAT', posix._have_functions)
    else:
        self.assertNotIn('HAVE_MKNODAT', posix._have_functions)
        with self.assertRaisesRegex(NotImplementedError, 'dir_fd unavailable'):
            os.mknod('path', dir_fd=0)
