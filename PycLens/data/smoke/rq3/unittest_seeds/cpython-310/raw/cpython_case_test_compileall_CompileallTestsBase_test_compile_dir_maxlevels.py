# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_compile_dir_maxlevels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    depth = 3
    path = self.directory
    for i in range(1, depth + 1):
        path = os.path.join(path, f'dir_{i}')
        source = os.path.join(path, 'script.py')
        os.mkdir(path)
        shutil.copyfile(self.source_path, source)
    pyc_filename = importlib.util.cache_from_source(source)
    compileall.compile_dir(self.directory, quiet=True, maxlevels=depth - 1)
    self.assertFalse(os.path.isfile(pyc_filename))
    compileall.compile_dir(self.directory, quiet=True, maxlevels=depth)
    self.assertTrue(os.path.isfile(pyc_filename))
