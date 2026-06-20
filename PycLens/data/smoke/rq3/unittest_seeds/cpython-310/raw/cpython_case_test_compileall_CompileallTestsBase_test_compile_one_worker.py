# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_compile_one_worker

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compileall.compile_dir(self.directory, quiet=True)
    self.assertFalse(pool_mock.called)
    self.assertTrue(compile_file_mock.called)
