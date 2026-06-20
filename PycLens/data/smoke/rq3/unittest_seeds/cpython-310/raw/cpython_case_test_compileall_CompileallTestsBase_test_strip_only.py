# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CompileallTestsBase_test_strip_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fullpath = ['test', 'build', 'real', 'path']
    path = os.path.join(self.directory, *fullpath)
    os.makedirs(path)
    script = script_helper.make_script(path, 'test', '1 / 0')
    bc = importlib.util.cache_from_source(script)
    stripdir = os.path.join(self.directory, *fullpath[:2])
    compileall.compile_dir(path, quiet=True, stripdir=stripdir)
    (rc, out, err) = script_helper.assert_python_failure(bc)
    expected_in = os.path.join(*fullpath[2:])
    self.assertIn(expected_in, str(err, encoding=sys.getdefaultencoding()))
    self.assertNotIn(stripdir, str(err, encoding=sys.getdefaultencoding()))
