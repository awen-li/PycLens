# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copy_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src = os.path.join(tmp_dir, 'foo')
    dst = os.path.join(tmp_dir, 'bar')
    src_link = os.path.join(tmp_dir, 'baz')
    write_file(src, 'foo')
    os.symlink(src, src_link)
    if hasattr(os, 'lchmod'):
        os.lchmod(src_link, stat.S_IRWXU | stat.S_IRWXO)
    shutil.copy(src_link, dst, follow_symlinks=True)
    self.assertFalse(os.path.islink(dst))
    self.assertEqual(read_file(src), read_file(dst))
    os.remove(dst)
    shutil.copy(src_link, dst, follow_symlinks=False)
    self.assertTrue(os.path.islink(dst))
    self.assertEqual(os.readlink(dst), os.readlink(src_link))
    if hasattr(os, 'lchmod'):
        self.assertEqual(os.lstat(src_link).st_mode, os.lstat(dst).st_mode)
