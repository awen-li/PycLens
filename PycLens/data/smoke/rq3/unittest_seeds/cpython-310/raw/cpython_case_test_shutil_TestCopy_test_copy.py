# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (file1, file2) = self._copy_file(shutil.copy)
    self.assertTrue(os.path.exists(file2))
    self.assertEqual(os.stat(file1).st_mode, os.stat(file2).st_mode)
