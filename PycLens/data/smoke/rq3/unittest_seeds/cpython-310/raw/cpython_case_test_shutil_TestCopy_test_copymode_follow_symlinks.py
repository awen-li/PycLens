# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copymode_follow_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src = os.path.join(tmp_dir, 'foo')
    dst = os.path.join(tmp_dir, 'bar')
    src_link = os.path.join(tmp_dir, 'baz')
    dst_link = os.path.join(tmp_dir, 'quux')
    write_file(src, 'foo')
    write_file(dst, 'foo')
    os.symlink(src, src_link)
    os.symlink(dst, dst_link)
    os.chmod(src, stat.S_IRWXU | stat.S_IRWXG)
    os.chmod(dst, stat.S_IRWXO)
    self.assertNotEqual(os.stat(src).st_mode, os.stat(dst).st_mode)
    shutil.copymode(src, dst)
    self.assertEqual(os.stat(src).st_mode, os.stat(dst).st_mode)
    if os.name != 'nt':
        os.chmod(dst, stat.S_IRWXO)
        shutil.copymode(src_link, dst)
        self.assertEqual(os.stat(src).st_mode, os.stat(dst).st_mode)
        os.chmod(dst, stat.S_IRWXO)
        shutil.copymode(src, dst_link)
        self.assertEqual(os.stat(src).st_mode, os.stat(dst).st_mode)
        os.chmod(dst, stat.S_IRWXO)
        shutil.copymode(src_link, dst_link)
        self.assertEqual(os.stat(src).st_mode, os.stat(dst).st_mode)
