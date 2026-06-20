# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_larger_than_32_bit_times

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.utime(self.source_path, (2 ** 35, 2 ** 35))
    except (OverflowError, OSError):
        self.skipTest("filesystem doesn't support large timestamps")
    with contextlib.redirect_stdout(io.StringIO()):
        self.assertTrue(compileall.compile_file(self.source_path))
