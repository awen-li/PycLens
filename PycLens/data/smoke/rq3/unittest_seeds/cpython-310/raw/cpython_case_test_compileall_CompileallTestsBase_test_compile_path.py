# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_compile_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with test.test_importlib.util.import_state(path=[self.directory]):
        self.assertTrue(compileall.compile_path(quiet=2))
    with test.test_importlib.util.import_state(path=[self.directory]):
        self.add_bad_source_file()
        self.assertFalse(compileall.compile_path(skip_curdir=False, force=True, quiet=2))
