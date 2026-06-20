# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_nowindows

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-n', '--nowindows'):
        with self.subTest(opt=opt):
            with contextlib.redirect_stderr(io.StringIO()) as stderr:
                ns = libregrtest._parse_args([opt])
            self.assertTrue(ns.nowindows)
            err = stderr.getvalue()
            self.assertIn('the --nowindows (-n) option is deprecated', err)
