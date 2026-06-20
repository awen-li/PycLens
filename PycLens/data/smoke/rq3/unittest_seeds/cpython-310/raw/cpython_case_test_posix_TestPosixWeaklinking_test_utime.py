# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_utime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_FUTIMENS')
    self._verify_available('HAVE_UTIMENSAT')
    if self.mac_ver >= (10, 13):
        self.assertIn('HAVE_FUTIMENS', posix._have_functions)
        self.assertIn('HAVE_UTIMENSAT', posix._have_functions)
    else:
        self.assertNotIn('HAVE_FUTIMENS', posix._have_functions)
        self.assertNotIn('HAVE_UTIMENSAT', posix._have_functions)
        with self.assertRaisesRegex(NotImplementedError, 'dir_fd unavailable'):
            os.utime('path', dir_fd=0)
