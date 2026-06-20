# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_compile_file_encoding_fallback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.add_bad_source_file()
    with contextlib.redirect_stdout(io.StringIO()):
        self.assertFalse(compileall.compile_file(self.bad_source_path))
