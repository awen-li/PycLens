# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    dst_dir = os.path.join(self.mkdtemp(), 'destination')
    self.addCleanup(shutil.rmtree, src_dir)
    self.addCleanup(shutil.rmtree, os.path.dirname(dst_dir))
    write_file((src_dir, 'test.txt'), '123')
    os.mkdir(os.path.join(src_dir, 'test_dir'))
    write_file((src_dir, 'test_dir', 'test.txt'), '456')
    shutil.copytree(src_dir, dst_dir)
    self.assertTrue(os.path.isfile(os.path.join(dst_dir, 'test.txt')))
    self.assertTrue(os.path.isdir(os.path.join(dst_dir, 'test_dir')))
    self.assertTrue(os.path.isfile(os.path.join(dst_dir, 'test_dir', 'test.txt')))
    actual = read_file((dst_dir, 'test.txt'))
    self.assertEqual(actual, '123')
    actual = read_file((dst_dir, 'test_dir', 'test.txt'))
    self.assertEqual(actual, '456')
