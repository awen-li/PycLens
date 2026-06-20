# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_d_compile_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script_helper.make_script(self.pkgdir, 'crunchyfrog', 'bad(syntax')
    (rc, out, err) = self.assertRunNotOK('-q', '-d', 'dinsdale', self.pkgdir)
    self.assertRegex(out, b'File "dinsdale')
