# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_link

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_LINKAT')
    if self.mac_ver >= (10, 10):
        self.assertIn('HAVE_LINKAT', posix._have_functions)
    else:
        self.assertNotIn('HAVE_LINKAT', posix._have_functions)
        with self.assertRaisesRegex(NotImplementedError, 'src_dir_fd unavailable'):
            os.link('source', 'target', src_dir_fd=0)
        with self.assertRaisesRegex(NotImplementedError, 'dst_dir_fd unavailable'):
            os.link('source', 'target', dst_dir_fd=0)
        with self.assertRaisesRegex(NotImplementedError, 'src_dir_fd unavailable'):
            os.link('source', 'target', src_dir_fd=0, dst_dir_fd=0)
        with os_helper.temp_dir() as base_path:
            link_path = os.path.join(base_path, 'link')
            target_path = os.path.join(base_path, 'target')
            source_path = os.path.join(base_path, 'source')
            with open(source_path, 'w') as fp:
                fp.write('data')
            os.symlink('target', link_path)
            with self.assertRaises(FileExistsError):
                os.link(source_path, link_path, follow_symlinks=True)
            with self.assertRaises(FileExistsError):
                os.link(source_path, link_path, follow_symlinks=False)
