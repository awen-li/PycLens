# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_unlink_rmdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_UNLINKAT')
    if self.mac_ver >= (10, 10):
        self.assertIn('HAVE_UNLINKAT', posix._have_functions)
    else:
        self.assertNotIn('HAVE_UNLINKAT', posix._have_functions)
        with self.assertRaisesRegex(NotImplementedError, 'dir_fd unavailable'):
            os.unlink('path', dir_fd=0)
        with self.assertRaisesRegex(NotImplementedError, 'dir_fd unavailable'):
            os.rmdir('path', dir_fd=0)
