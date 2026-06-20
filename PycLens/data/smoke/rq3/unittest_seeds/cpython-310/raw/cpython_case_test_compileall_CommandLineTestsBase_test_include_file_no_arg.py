# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_include_file_no_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f1 = script_helper.make_script(self.pkgdir, 'f1', '')
    f2 = script_helper.make_script(self.pkgdir, 'f2', '')
    f3 = script_helper.make_script(self.pkgdir, 'f3', '')
    f4 = script_helper.make_script(self.pkgdir, 'f4', '')
    with open(os.path.join(self.directory, 'l1'), 'w', encoding='utf-8') as l1:
        l1.write(os.path.join(self.pkgdir, 'f2.py') + os.linesep)
    self.assertRunOK('-i', os.path.join(self.directory, 'l1'))
    self.assertNotCompiled(f1)
    self.assertCompiled(f2)
    self.assertNotCompiled(f3)
    self.assertNotCompiled(f4)
