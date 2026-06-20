# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_legacy_paths

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRunOK('-b', '-q', self.pkgdir)
    self.assertFalse(os.path.exists(self.pkgdir_cachedir))
    expected = sorted(['__init__.py', '__init__.pyc', 'bar.py', 'bar.pyc'])
    self.assertEqual(sorted(os.listdir(self.pkgdir)), expected)
