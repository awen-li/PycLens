# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_symlink_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    dst_dir = os.path.join(self.mkdtemp(), 'destination')
    os.mkdir(os.path.join(src_dir, 'real_dir'))
    with open(os.path.join(src_dir, 'real_dir', 'test.txt'), 'wb'):
        pass
    os.symlink(os.path.join(src_dir, 'real_dir'), os.path.join(src_dir, 'link_to_dir'), target_is_directory=True)
    shutil.copytree(src_dir, dst_dir, symlinks=False)
    self.assertFalse(os.path.islink(os.path.join(dst_dir, 'link_to_dir')))
    self.assertIn('test.txt', os.listdir(os.path.join(dst_dir, 'link_to_dir')))
    dst_dir = os.path.join(self.mkdtemp(), 'destination2')
    shutil.copytree(src_dir, dst_dir, symlinks=True)
    self.assertTrue(os.path.islink(os.path.join(dst_dir, 'link_to_dir')))
    self.assertIn('test.txt', os.listdir(os.path.join(dst_dir, 'link_to_dir')))
