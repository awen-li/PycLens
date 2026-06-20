# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestRmTree_test_rmtree_dont_delete_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (handle, path) = tempfile.mkstemp(dir=self.mkdtemp())
    os.close(handle)
    self.assertRaises(NotADirectoryError, shutil.rmtree, path)
    os.remove(path)
