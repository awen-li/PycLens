# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_failfast

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-G', '--failfast'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, '-v'])
            self.assertTrue(ns.failfast)
            ns = libregrtest._parse_args([opt, '-W'])
            self.assertTrue(ns.failfast)
            self.checkError([opt], '-G/--failfast needs either -v or -W')
