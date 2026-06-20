# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_compile_dir_pathlike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(os.path.isfile(self.bc_path))
    with support.captured_stdout() as stdout:
        compileall.compile_dir(pathlib.Path(self.directory))
    line = stdout.getvalue().splitlines()[0]
    self.assertRegex(line, 'Listing ([^WindowsPath|PosixPath].*)')
    self.assertTrue(os.path.isfile(self.bc_path))
