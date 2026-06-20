# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_relative_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    py_compile.compile(os.path.relpath(self.source_path), os.path.relpath(self.pyc_path))
    self.assertTrue(os.path.exists(self.pyc_path))
    self.assertFalse(os.path.exists(self.cache_path))
