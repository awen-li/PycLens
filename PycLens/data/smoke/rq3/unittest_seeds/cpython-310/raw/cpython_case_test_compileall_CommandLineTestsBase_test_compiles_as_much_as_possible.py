# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_compiles_as_much_as_possible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bingfn = script_helper.make_script(self.pkgdir, 'bing', 'syntax(error')
    (rc, out, err) = self.assertRunNotOK('nosuchfile', self.initfn, bingfn, self.barfn)
    self.assertRegex(out, b'rror')
    self.assertNotCompiled(bingfn)
    self.assertCompiled(self.initfn)
    self.assertCompiled(self.barfn)
