# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copyfile_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src = os.path.join(tmp_dir, 'src')
    dst = os.path.join(tmp_dir, 'dst')
    dst_link = os.path.join(tmp_dir, 'dst_link')
    link = os.path.join(tmp_dir, 'link')
    write_file(src, 'foo')
    os.symlink(src, link)
    shutil.copyfile(link, dst_link, follow_symlinks=False)
    self.assertTrue(os.path.islink(dst_link))
    self.assertEqual(os.readlink(link), os.readlink(dst_link))
    shutil.copyfile(link, dst)
    self.assertFalse(os.path.islink(dst))
