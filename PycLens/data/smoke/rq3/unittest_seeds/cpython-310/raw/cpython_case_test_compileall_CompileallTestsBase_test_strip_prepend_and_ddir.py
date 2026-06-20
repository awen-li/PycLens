# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_strip_prepend_and_ddir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fullpath = ['test', 'build', 'real', 'path', 'ddir']
    path = os.path.join(self.directory, *fullpath)
    os.makedirs(path)
    script_helper.make_script(path, 'test', '1 / 0')
    with self.assertRaises(ValueError):
        compileall.compile_dir(path, quiet=True, ddir='/bar', stripdir='/foo', prependdir='/bar')
