# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_dangling_symlinks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    valid_file = os.path.join(src_dir, 'test.txt')
    write_file(valid_file, 'abc')
    dir_a = os.path.join(src_dir, 'dir_a')
    os.mkdir(dir_a)
    for d in (src_dir, dir_a):
        os.symlink('IDONTEXIST', os.path.join(d, 'broken'))
        os.symlink(valid_file, os.path.join(d, 'valid'))
    dst_dir = os.path.join(self.mkdtemp(), 'destination')
    self.assertRaises(Error, shutil.copytree, src_dir, dst_dir)
    dst_dir = os.path.join(self.mkdtemp(), 'destination2')
    shutil.copytree(src_dir, dst_dir, ignore_dangling_symlinks=True)
    for (root, dirs, files) in os.walk(dst_dir):
        self.assertNotIn('broken', files)
        self.assertIn('valid', files)
    dst_dir = os.path.join(self.mkdtemp(), 'destination3')
    shutil.copytree(src_dir, dst_dir, symlinks=True)
    self.assertIn('test.txt', os.listdir(dst_dir))
