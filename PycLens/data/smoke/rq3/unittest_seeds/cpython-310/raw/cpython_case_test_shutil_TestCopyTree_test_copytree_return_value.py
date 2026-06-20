# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_return_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    dst_dir = src_dir + 'dest'
    self.addCleanup(shutil.rmtree, dst_dir, True)
    src = os.path.join(src_dir, 'foo')
    write_file(src, 'foo')
    rv = shutil.copytree(src_dir, dst_dir)
    self.assertEqual(['foo'], os.listdir(rv))
