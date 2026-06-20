# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_compile_files

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fn in (self.bc_path, self.bc_path2):
        try:
            os.unlink(fn)
        except:
            pass
    self.assertTrue(compileall.compile_file(self.source_path, force=False, quiet=True))
    self.assertTrue(os.path.isfile(self.bc_path) and (not os.path.isfile(self.bc_path2)))
    os.unlink(self.bc_path)
    self.assertTrue(compileall.compile_dir(self.directory, force=False, quiet=True))
    self.assertTrue(os.path.isfile(self.bc_path) and os.path.isfile(self.bc_path2))
    os.unlink(self.bc_path)
    os.unlink(self.bc_path2)
    self.add_bad_source_file()
    self.assertFalse(compileall.compile_file(self.bad_source_path, force=False, quiet=2))
    self.assertFalse(compileall.compile_dir(self.directory, force=False, quiet=2))
