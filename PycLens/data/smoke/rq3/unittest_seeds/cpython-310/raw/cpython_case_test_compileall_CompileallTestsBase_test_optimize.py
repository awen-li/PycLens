# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_optimize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (optimize, opt) = (1, 1) if __debug__ else (0, '')
    compileall.compile_dir(self.directory, quiet=True, optimize=optimize)
    cached = importlib.util.cache_from_source(self.source_path, optimization=opt)
    self.assertTrue(os.path.isfile(cached))
    cached2 = importlib.util.cache_from_source(self.source_path2, optimization=opt)
    self.assertTrue(os.path.isfile(cached2))
    cached3 = importlib.util.cache_from_source(self.source_path3, optimization=opt)
    self.assertTrue(os.path.isfile(cached3))
