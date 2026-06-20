# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_symlink_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkg = os.path.join(self.pkgdir, 'spam')
    script_helper.make_pkg(pkg)
    os.symlink('.', os.path.join(pkg, 'evil'))
    os.symlink('.', os.path.join(pkg, 'evil2'))
    self.assertRunOK('-q', self.pkgdir)
    self.assertCompiled(os.path.join(self.pkgdir, 'spam', 'evil', 'evil2', '__init__.py'))
