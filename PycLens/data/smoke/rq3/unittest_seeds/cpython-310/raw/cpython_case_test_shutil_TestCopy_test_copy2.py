# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopy_test_copy2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (file1, file2) = self._copy_file(shutil.copy2)
    self.assertTrue(os.path.exists(file2))
    file1_stat = os.stat(file1)
    file2_stat = os.stat(file2)
    self.assertEqual(file1_stat.st_mode, file2_stat.st_mode)
    for attr in ('st_atime', 'st_mtime'):
        self.assertLessEqual(getattr(file1_stat, attr), getattr(file2_stat, attr) + 1)
    if hasattr(os, 'chflags') and hasattr(file1_stat, 'st_flags'):
        self.assertEqual(getattr(file1_stat, 'st_flags'), getattr(file2_stat, 'st_flags'))
