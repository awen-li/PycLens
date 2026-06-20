# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_workers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bar2fn = script_helper.make_script(self.directory, 'bar2', '')
    files = []
    for suffix in range(5):
        pkgdir = os.path.join(self.directory, 'foo{}'.format(suffix))
        os.mkdir(pkgdir)
        fn = script_helper.make_script(pkgdir, '__init__', '')
        files.append(script_helper.make_script(pkgdir, 'bar2', ''))
    self.assertRunOK(self.directory, '-j', '0')
    self.assertCompiled(bar2fn)
    for file in files:
        self.assertCompiled(file)
