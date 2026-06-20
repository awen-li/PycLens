# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_dirs_exist_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    dst_dir = self.mkdtemp()
    self.addCleanup(shutil.rmtree, src_dir)
    self.addCleanup(shutil.rmtree, dst_dir)
    write_file((src_dir, 'nonexisting.txt'), '123')
    os.mkdir(os.path.join(src_dir, 'existing_dir'))
    os.mkdir(os.path.join(dst_dir, 'existing_dir'))
    write_file((dst_dir, 'existing_dir', 'existing.txt'), 'will be replaced')
    write_file((src_dir, 'existing_dir', 'existing.txt'), 'has been replaced')
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
    self.assertTrue(os.path.isfile(os.path.join(dst_dir, 'nonexisting.txt')))
    self.assertTrue(os.path.isdir(os.path.join(dst_dir, 'existing_dir')))
    self.assertTrue(os.path.isfile(os.path.join(dst_dir, 'existing_dir', 'existing.txt')))
    actual = read_file((dst_dir, 'nonexisting.txt'))
    self.assertEqual(actual, '123')
    actual = read_file((dst_dir, 'existing_dir', 'existing.txt'))
    self.assertEqual(actual, 'has been replaced')
    with self.assertRaises(FileExistsError):
        shutil.copytree(src_dir, dst_dir, dirs_exist_ok=False)
