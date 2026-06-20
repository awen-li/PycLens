# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_recursion_control

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    subpackage = os.path.join(self.pkgdir, 'spam')
    os.mkdir(subpackage)
    subinitfn = script_helper.make_script(subpackage, '__init__', '')
    hamfn = script_helper.make_script(subpackage, 'ham', '')
    self.assertRunOK('-q', '-l', self.pkgdir)
    self.assertNotCompiled(subinitfn)
    self.assertFalse(os.path.exists(os.path.join(subpackage, '__pycache__')))
    self.assertRunOK('-q', self.pkgdir)
    self.assertCompiled(subinitfn)
    self.assertCompiled(hamfn)
