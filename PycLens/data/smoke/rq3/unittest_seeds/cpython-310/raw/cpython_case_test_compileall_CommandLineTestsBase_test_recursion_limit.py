# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_recursion_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    subpackage = os.path.join(self.pkgdir, 'spam')
    subpackage2 = os.path.join(subpackage, 'ham')
    subpackage3 = os.path.join(subpackage2, 'eggs')
    for pkg in (subpackage, subpackage2, subpackage3):
        script_helper.make_pkg(pkg)
    subinitfn = os.path.join(subpackage, '__init__.py')
    hamfn = script_helper.make_script(subpackage, 'ham', '')
    spamfn = script_helper.make_script(subpackage2, 'spam', '')
    eggfn = script_helper.make_script(subpackage3, 'egg', '')
    self.assertRunOK('-q', '-r 0', self.pkgdir)
    self.assertNotCompiled(subinitfn)
    self.assertFalse(os.path.exists(os.path.join(subpackage, '__pycache__')))
    self.assertRunOK('-q', '-r 1', self.pkgdir)
    self.assertCompiled(subinitfn)
    self.assertCompiled(hamfn)
    self.assertNotCompiled(spamfn)
    self.assertRunOK('-q', '-r 2', self.pkgdir)
    self.assertCompiled(subinitfn)
    self.assertCompiled(hamfn)
    self.assertCompiled(spamfn)
    self.assertNotCompiled(eggfn)
    self.assertRunOK('-q', '-r 5', self.pkgdir)
    self.assertCompiled(subinitfn)
    self.assertCompiled(hamfn)
    self.assertCompiled(spamfn)
    self.assertCompiled(eggfn)
