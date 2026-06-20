# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_quiet

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    noisy = self.assertRunOK(self.pkgdir)
    quiet = self.assertRunOK('-q', self.pkgdir)
    self.assertNotEqual(b'', noisy)
    self.assertEqual(b'', quiet)
