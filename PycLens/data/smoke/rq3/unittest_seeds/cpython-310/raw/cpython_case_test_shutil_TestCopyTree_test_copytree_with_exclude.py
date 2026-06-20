# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_with_exclude

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    join = os.path.join
    exists = os.path.exists
    src_dir = self.mkdtemp()
    try:
        dst_dir = join(self.mkdtemp(), 'destination')
        write_file((src_dir, 'test.txt'), '123')
        write_file((src_dir, 'test.tmp'), '123')
        os.mkdir(join(src_dir, 'test_dir'))
        write_file((src_dir, 'test_dir', 'test.txt'), '456')
        os.mkdir(join(src_dir, 'test_dir2'))
        write_file((src_dir, 'test_dir2', 'test.txt'), '456')
        os.mkdir(join(src_dir, 'test_dir2', 'subdir'))
        os.mkdir(join(src_dir, 'test_dir2', 'subdir2'))
        write_file((src_dir, 'test_dir2', 'subdir', 'test.txt'), '456')
        write_file((src_dir, 'test_dir2', 'subdir2', 'test.py'), '456')
        try:
            patterns = shutil.ignore_patterns('*.tmp', 'test_dir2')
            shutil.copytree(src_dir, dst_dir, ignore=patterns)
            self.assertTrue(exists(join(dst_dir, 'test.txt')))
            self.assertFalse(exists(join(dst_dir, 'test.tmp')))
            self.assertFalse(exists(join(dst_dir, 'test_dir2')))
        finally:
            shutil.rmtree(dst_dir)
        try:
            patterns = shutil.ignore_patterns('*.tmp', 'subdir*')
            shutil.copytree(src_dir, dst_dir, ignore=patterns)
            self.assertFalse(exists(join(dst_dir, 'test.tmp')))
            self.assertFalse(exists(join(dst_dir, 'test_dir2', 'subdir2')))
            self.assertFalse(exists(join(dst_dir, 'test_dir2', 'subdir')))
        finally:
            shutil.rmtree(dst_dir)
        try:

            def _filter(src, names):
                res = []
                for name in names:
                    path = os.path.join(src, name)
                    if os.path.isdir(path) and path.split()[-1] == 'subdir':
                        res.append(name)
                    elif os.path.splitext(path)[-1] in '.py':
                        res.append(name)
                return res
            shutil.copytree(src_dir, dst_dir, ignore=_filter)
            self.assertFalse(exists(join(dst_dir, 'test_dir2', 'subdir2', 'test.py')))
            self.assertFalse(exists(join(dst_dir, 'test_dir2', 'subdir')))
        finally:
            shutil.rmtree(dst_dir)
    finally:
        shutil.rmtree(src_dir)
        shutil.rmtree(os.path.dirname(dst_dir))
