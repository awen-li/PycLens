# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileCLITestCase_test_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.pycompilecmd('-', input=self.source_path)
    self.assertEqual(result.returncode, 0)
    self.assertEqual(result.stdout, b'')
    self.assertEqual(result.stderr, b'')
    self.assertTrue(os.path.exists(self.cache_path))
