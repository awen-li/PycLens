# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_uses_safe_fd_version_if_available

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _use_fd_functions = {os.open, os.stat, os.unlink, os.rmdir} <= os.supports_dir_fd and os.listdir in os.supports_fd and (os.stat in os.supports_follow_symlinks)
    if _use_fd_functions:
        self.assertTrue(shutil._use_fd_functions)
        self.assertTrue(shutil.rmtree.avoids_symlink_attacks)
        tmp_dir = self.mkdtemp()
        d = os.path.join(tmp_dir, 'a')
        os.mkdir(d)
        try:
            real_rmtree = shutil._rmtree_safe_fd

            class Called(Exception):
                pass

            def _raiser(*args, **kwargs):
                raise Called
            shutil._rmtree_safe_fd = _raiser
            self.assertRaises(Called, shutil.rmtree, d)
        finally:
            shutil._rmtree_safe_fd = real_rmtree
    else:
        self.assertFalse(shutil._use_fd_functions)
        self.assertFalse(shutil.rmtree.avoids_symlink_attacks)
