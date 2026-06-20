# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_source_date_epoch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    py_compile.compile(self.source_path, self.pyc_path)
    self.assertTrue(os.path.exists(self.pyc_path))
    self.assertFalse(os.path.exists(self.cache_path))
    with open(self.pyc_path, 'rb') as fp:
        flags = importlib._bootstrap_external._classify_pyc(fp.read(), 'test', {})
    if os.environ.get('SOURCE_DATE_EPOCH'):
        expected_flags = 3
    else:
        expected_flags = 0
    self.assertEqual(flags, expected_flags)
