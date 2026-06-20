# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_rename_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_RENAMEAT')
    if self.mac_ver >= (10, 10):
        self.assertIn('HAVE_RENAMEAT', posix._have_functions)
    else:
        self.assertNotIn('HAVE_RENAMEAT', posix._have_functions)
        with self.assertRaisesRegex(NotImplementedError, 'src_dir_fd and dst_dir_fd unavailable'):
            os.rename('a', 'b', src_dir_fd=0)
        with self.assertRaisesRegex(NotImplementedError, 'src_dir_fd and dst_dir_fd unavailable'):
            os.rename('a', 'b', dst_dir_fd=0)
        with self.assertRaisesRegex(NotImplementedError, 'src_dir_fd and dst_dir_fd unavailable'):
            os.replace('a', 'b', src_dir_fd=0)
        with self.assertRaisesRegex(NotImplementedError, 'src_dir_fd and dst_dir_fd unavailable'):
            os.replace('a', 'b', dst_dir_fd=0)
