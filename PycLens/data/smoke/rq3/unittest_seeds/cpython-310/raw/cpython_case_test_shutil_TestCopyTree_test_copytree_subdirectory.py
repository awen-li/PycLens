# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_subdirectory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base_dir = self.mkdtemp()
    self.addCleanup(shutil.rmtree, base_dir, ignore_errors=True)
    src_dir = os.path.join(base_dir, 't', 'pg')
    dst_dir = os.path.join(src_dir, 'somevendor', '1.0')
    os.makedirs(src_dir)
    src = os.path.join(src_dir, 'pol')
    write_file(src, 'pol')
    rv = shutil.copytree(src_dir, dst_dir)
    self.assertEqual(['pol'], os.listdir(rv))
