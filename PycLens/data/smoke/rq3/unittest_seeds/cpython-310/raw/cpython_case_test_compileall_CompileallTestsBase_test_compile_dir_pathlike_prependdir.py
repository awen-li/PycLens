# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_compile_dir_pathlike_prependdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(os.path.isfile(self.bc_path))
    self.assertTrue(compileall.compile_dir(pathlib.Path(self.directory), prependdir=pathlib.Path('prependdir_path'), quiet=2))
    self.assertTrue(os.path.isfile(self.bc_path))
