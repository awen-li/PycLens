# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_retains_permissions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp_dir = self.mkdtemp()
    src_dir = os.path.join(tmp_dir, 'source')
    os.mkdir(src_dir)
    dst_dir = os.path.join(tmp_dir, 'destination')
    self.addCleanup(shutil.rmtree, tmp_dir)
    os.chmod(src_dir, 511)
    write_file((src_dir, 'permissive.txt'), '123')
    os.chmod(os.path.join(src_dir, 'permissive.txt'), 511)
    write_file((src_dir, 'restrictive.txt'), '456')
    os.chmod(os.path.join(src_dir, 'restrictive.txt'), 384)
    restrictive_subdir = tempfile.mkdtemp(dir=src_dir)
    self.addCleanup(os_helper.rmtree, restrictive_subdir)
    os.chmod(restrictive_subdir, 384)
    shutil.copytree(src_dir, dst_dir)
    self.assertEqual(os.stat(src_dir).st_mode, os.stat(dst_dir).st_mode)
    self.assertEqual(os.stat(os.path.join(src_dir, 'permissive.txt')).st_mode, os.stat(os.path.join(dst_dir, 'permissive.txt')).st_mode)
    self.assertEqual(os.stat(os.path.join(src_dir, 'restrictive.txt')).st_mode, os.stat(os.path.join(dst_dir, 'restrictive.txt')).st_mode)
    restrictive_subdir_dst = os.path.join(dst_dir, os.path.split(restrictive_subdir)[1])
    self.assertEqual(os.stat(restrictive_subdir).st_mode, os.stat(restrictive_subdir_dst).st_mode)
