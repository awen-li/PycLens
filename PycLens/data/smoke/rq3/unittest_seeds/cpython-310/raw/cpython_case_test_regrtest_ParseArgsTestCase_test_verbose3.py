# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_verbose3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-W', '--verbose3'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt])
            self.assertTrue(ns.verbose3)
