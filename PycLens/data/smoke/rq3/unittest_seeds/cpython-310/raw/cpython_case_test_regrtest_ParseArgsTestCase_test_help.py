# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-h', '--help'):
        with self.subTest(opt=opt):
            with support.captured_stdout() as out, self.assertRaises(SystemExit):
                libregrtest._parse_args([opt])
            self.assertIn('Run Python regression tests.', out.getvalue())
