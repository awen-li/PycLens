# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src_dir = os.path.join(tmp_dir, 'src')
    dst_dir = os.path.join(tmp_dir, 'dst')
    sub_dir = os.path.join(src_dir, 'sub')
    os.mkdir(src_dir)
    os.mkdir(sub_dir)
    write_file((src_dir, 'file.txt'), 'foo')
    src_link = os.path.join(sub_dir, 'link')
    dst_link = os.path.join(dst_dir, 'sub/link')
    os.symlink(os.path.join(src_dir, 'file.txt'), src_link)
    if hasattr(os, 'lchmod'):
        os.lchmod(src_link, stat.S_IRWXU | stat.S_IRWXO)
    if hasattr(os, 'lchflags') and hasattr(stat, 'UF_NODUMP'):
        os.lchflags(src_link, stat.UF_NODUMP)
    src_stat = os.lstat(src_link)
    shutil.copytree(src_dir, dst_dir, symlinks=True)
    self.assertTrue(os.path.islink(os.path.join(dst_dir, 'sub', 'link')))
    actual = os.readlink(os.path.join(dst_dir, 'sub', 'link'))
    if os.name == 'nt' and actual.startswith('\\\\?\\'):
        actual = actual[4:]
    self.assertEqual(actual, os.path.join(src_dir, 'file.txt'))
    dst_stat = os.lstat(dst_link)
    if hasattr(os, 'lchmod'):
        self.assertEqual(dst_stat.st_mode, src_stat.st_mode)
    if hasattr(os, 'lchflags'):
        self.assertEqual(dst_stat.st_flags, src_stat.st_flags)
