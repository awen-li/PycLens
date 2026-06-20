# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileCLITestCase_test_with_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, stdout, stderr) = self.pycompilecmd(self.source_path, self.source_path)
    self.assertEqual(rc, 0)
    self.assertEqual(stdout, b'')
    self.assertEqual(stderr, b'')
    self.assertTrue(os.path.exists(self.cache_path))
