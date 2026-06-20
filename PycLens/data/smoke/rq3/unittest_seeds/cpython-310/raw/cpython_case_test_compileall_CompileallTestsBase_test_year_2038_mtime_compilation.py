# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_year_2038_mtime_compilation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.utime(self.source_path, (2 ** 32 - 1, 2 ** 32 - 1))
    except (OverflowError, OSError):
        self.skipTest("filesystem doesn't support timestamps near 2**32")
    with contextlib.redirect_stdout(io.StringIO()):
        self.assertTrue(compileall.compile_file(self.source_path))
