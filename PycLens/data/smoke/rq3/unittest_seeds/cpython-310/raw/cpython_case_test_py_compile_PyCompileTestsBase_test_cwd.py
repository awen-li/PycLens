# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.change_cwd(self.directory):
        py_compile.compile(os.path.basename(self.source_path), os.path.basename(self.pyc_path))
    self.assertTrue(os.path.exists(self.pyc_path))
    self.assertFalse(os.path.exists(self.cache_path))
