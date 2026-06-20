# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_symlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_SYMLINKAT')
    if self.mac_ver >= (10, 10):
        self.assertIn('HAVE_SYMLINKAT', posix._have_functions)
    else:
        self.assertNotIn('HAVE_SYMLINKAT', posix._have_functions)
        with self.assertRaisesRegex(NotImplementedError, 'dir_fd unavailable'):
            os.symlink('a', 'b', dir_fd=0)
