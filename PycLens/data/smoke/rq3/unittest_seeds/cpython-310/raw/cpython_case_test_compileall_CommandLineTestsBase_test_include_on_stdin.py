# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_include_on_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f1 = script_helper.make_script(self.pkgdir, 'f1', '')
    f2 = script_helper.make_script(self.pkgdir, 'f2', '')
    f3 = script_helper.make_script(self.pkgdir, 'f3', '')
    f4 = script_helper.make_script(self.pkgdir, 'f4', '')
    p = script_helper.spawn_python(*self._get_run_args(()) + ['-i', '-'])
    p.stdin.write((f3 + os.linesep).encode('ascii'))
    script_helper.kill_python(p)
    self.assertNotCompiled(f1)
    self.assertNotCompiled(f2)
    self.assertCompiled(f3)
    self.assertNotCompiled(f4)
