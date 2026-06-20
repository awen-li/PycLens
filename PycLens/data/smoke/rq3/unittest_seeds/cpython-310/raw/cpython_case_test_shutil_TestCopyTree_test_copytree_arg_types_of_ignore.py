# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_arg_types_of_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    join = os.path.join
    exists = os.path.exists
    tmp_dir = self.mkdtemp()
    src_dir = join(tmp_dir, 'source')
    os.mkdir(join(src_dir))
    os.mkdir(join(src_dir, 'test_dir'))
    os.mkdir(os.path.join(src_dir, 'test_dir', 'subdir'))
    write_file((src_dir, 'test_dir', 'subdir', 'test.txt'), '456')
    invokations = []

    def _ignore(src, names):
        invokations.append(src)
        self.assertIsInstance(src, str)
        self.assertIsInstance(names, list)
        self.assertEqual(len(names), len(set(names)))
        for name in names:
            self.assertIsInstance(name, str)
        return []
    dst_dir = join(self.mkdtemp(), 'destination')
    shutil.copytree(src_dir, dst_dir, ignore=_ignore)
    self.assertTrue(exists(join(dst_dir, 'test_dir', 'subdir', 'test.txt')))
    dst_dir = join(self.mkdtemp(), 'destination')
    shutil.copytree(pathlib.Path(src_dir), dst_dir, ignore=_ignore)
    self.assertTrue(exists(join(dst_dir, 'test_dir', 'subdir', 'test.txt')))
    dst_dir = join(self.mkdtemp(), 'destination')
    src_dir_entry = list(os.scandir(tmp_dir))[0]
    self.assertIsInstance(src_dir_entry, os.DirEntry)
    shutil.copytree(src_dir_entry, dst_dir, ignore=_ignore)
    self.assertTrue(exists(join(dst_dir, 'test_dir', 'subdir', 'test.txt')))
    self.assertEqual(len(invokations), 9)
