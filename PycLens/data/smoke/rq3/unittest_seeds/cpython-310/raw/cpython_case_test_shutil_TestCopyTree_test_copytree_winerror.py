# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_winerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src_dir = self.mkdtemp()
    dst_dir = os.path.join(self.mkdtemp(), 'destination')
    self.addCleanup(shutil.rmtree, src_dir)
    self.addCleanup(shutil.rmtree, os.path.dirname(dst_dir))
    mock_patch.side_effect = PermissionError('ka-boom')
    with self.assertRaises(shutil.Error):
        shutil.copytree(src_dir, dst_dir)
