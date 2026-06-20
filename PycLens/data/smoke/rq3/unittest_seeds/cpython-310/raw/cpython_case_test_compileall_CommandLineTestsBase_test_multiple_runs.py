# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_multiple_runs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRunOK('-q', self.pkgdir)
    self.assertTrue(os.path.exists(self.pkgdir_cachedir))
    cachecachedir = os.path.join(self.pkgdir_cachedir, '__pycache__')
    self.assertFalse(os.path.exists(cachecachedir))
    self.assertRunOK('-q', self.pkgdir)
    self.assertTrue(os.path.exists(self.pkgdir_cachedir))
    self.assertFalse(os.path.exists(cachecachedir))
