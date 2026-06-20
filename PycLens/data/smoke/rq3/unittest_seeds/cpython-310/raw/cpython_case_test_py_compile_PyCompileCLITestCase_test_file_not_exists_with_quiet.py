# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileCLITestCase_test_file_not_exists_with_quiet

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    should_not_exists = os.path.join(os.path.dirname(__file__), 'should_not_exists.py')
    (rc, stdout, stderr) = self.pycompilecmd_failure('-q', self.source_path, should_not_exists)
    self.assertEqual(rc, 1)
    self.assertEqual(stdout, b'')
    self.assertEqual(stderr, b'')
