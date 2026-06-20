# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_special_func

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    dst_dir = os.path.join(self.mkdtemp(), 'destination')
    write_file((src_dir, 'test.txt'), '123')
    os.mkdir(os.path.join(src_dir, 'test_dir'))
    write_file((src_dir, 'test_dir', 'test.txt'), '456')
    copied = []

    def _copy(src, dst):
        copied.append((src, dst))
    shutil.copytree(src_dir, dst_dir, copy_function=_copy)
    self.assertEqual(len(copied), 2)
