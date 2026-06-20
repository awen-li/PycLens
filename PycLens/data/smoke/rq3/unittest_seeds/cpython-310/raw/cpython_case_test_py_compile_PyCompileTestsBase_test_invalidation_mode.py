# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_py_compile.py
# case: PyCompileTestsBase_test_invalidation_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    py_compile.compile(self.source_path, invalidation_mode=py_compile.PycInvalidationMode.CHECKED_HASH)
    with open(self.cache_path, 'rb') as fp:
        flags = importlib._bootstrap_external._classify_pyc(fp.read(), 'test', {})
    self.assertEqual(flags, 3)
    py_compile.compile(self.source_path, invalidation_mode=py_compile.PycInvalidationMode.UNCHECKED_HASH)
    with open(self.cache_path, 'rb') as fp:
        flags = importlib._bootstrap_external._classify_pyc(fp.read(), 'test', {})
    self.assertEqual(flags, 1)
