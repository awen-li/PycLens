# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_multiple_dirs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkgdir2 = os.path.join(self.directory, 'foo2')
    os.mkdir(pkgdir2)
    init2fn = script_helper.make_script(pkgdir2, '__init__', '')
    bar2fn = script_helper.make_script(pkgdir2, 'bar2', '')
    self.assertRunOK('-q', self.pkgdir, pkgdir2)
    self.assertCompiled(self.initfn)
    self.assertCompiled(self.barfn)
    self.assertCompiled(init2fn)
    self.assertCompiled(bar2fn)
