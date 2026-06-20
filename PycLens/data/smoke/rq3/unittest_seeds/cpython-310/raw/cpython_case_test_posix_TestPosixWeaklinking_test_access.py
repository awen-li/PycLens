# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_access

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_FACCESSAT')
    if self.mac_ver >= (10, 10):
        self.assertIn('HAVE_FACCESSAT', posix._have_functions)
    else:
        self.assertNotIn('HAVE_FACCESSAT', posix._have_functions)
        with self.assertRaisesRegex(NotImplementedError, 'dir_fd unavailable'):
            os.access('file', os.R_OK, dir_fd=0)
        with self.assertRaisesRegex(NotImplementedError, 'follow_symlinks unavailable'):
            os.access('file', os.R_OK, follow_symlinks=False)
        with self.assertRaisesRegex(NotImplementedError, 'effective_ids unavailable'):
            os.access('file', os.R_OK, effective_ids=True)
