# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_d_runtime_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bazfn = script_helper.make_script(self.pkgdir, 'baz', 'raise Exception')
    self.assertRunOK('-q', '-d', 'dinsdale', self.pkgdir)
    fn = script_helper.make_script(self.pkgdir, 'bing', 'import baz')
    pyc = importlib.util.cache_from_source(bazfn)
    os.rename(pyc, os.path.join(self.pkgdir, 'baz.pyc'))
    os.remove(bazfn)
    (rc, out, err) = script_helper.assert_python_failure(fn, __isolated=False)
    self.assertRegex(err, b'File "dinsdale')
