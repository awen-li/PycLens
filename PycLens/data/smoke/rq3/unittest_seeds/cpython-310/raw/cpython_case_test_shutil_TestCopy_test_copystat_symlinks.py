# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copystat_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src = os.path.join(tmp_dir, 'foo')
    dst = os.path.join(tmp_dir, 'bar')
    src_link = os.path.join(tmp_dir, 'baz')
    dst_link = os.path.join(tmp_dir, 'qux')
    write_file(src, 'foo')
    src_stat = os.stat(src)
    os.utime(src, (src_stat.st_atime, src_stat.st_mtime - 42.0))
    write_file(dst, 'bar')
    self.assertNotEqual(os.stat(src).st_mtime, os.stat(dst).st_mtime)
    os.symlink(src, src_link)
    os.symlink(dst, dst_link)
    if hasattr(os, 'lchmod'):
        os.lchmod(src_link, stat.S_IRWXO)
    if hasattr(os, 'lchflags') and hasattr(stat, 'UF_NODUMP'):
        os.lchflags(src_link, stat.UF_NODUMP)
    src_link_stat = os.lstat(src_link)
    if hasattr(os, 'lchmod'):
        shutil.copystat(src_link, dst_link, follow_symlinks=True)
        self.assertNotEqual(src_link_stat.st_mode, os.stat(dst).st_mode)
    shutil.copystat(src_link, dst_link, follow_symlinks=False)
    dst_link_stat = os.lstat(dst_link)
    if os.utime in os.supports_follow_symlinks:
        for attr in ('st_atime', 'st_mtime'):
            self.assertLessEqual(getattr(src_link_stat, attr), getattr(dst_link_stat, attr) + 1)
    if hasattr(os, 'lchmod'):
        self.assertEqual(src_link_stat.st_mode, dst_link_stat.st_mode)
    if hasattr(os, 'lchflags') and hasattr(src_link_stat, 'st_flags'):
        self.assertEqual(src_link_stat.st_flags, dst_link_stat.st_flags)
    shutil.copystat(src_link, dst, follow_symlinks=False)
    self.assertTrue(abs(os.stat(src).st_mtime - os.stat(dst).st_mtime) < 0.1)
