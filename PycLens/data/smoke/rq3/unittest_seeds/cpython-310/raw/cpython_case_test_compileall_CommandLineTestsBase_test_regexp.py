# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_regexp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRunOK('-q', '-x', 'ba[^\\\\/]*$', self.pkgdir)
    self.assertNotCompiled(self.barfn)
    self.assertCompiled(self.initfn)
