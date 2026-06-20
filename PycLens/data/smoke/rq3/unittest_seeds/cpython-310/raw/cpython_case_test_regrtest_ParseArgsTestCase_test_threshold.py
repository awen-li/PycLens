# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_threshold

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-t', '--threshold'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, '1000'])
            self.assertEqual(ns.threshold, 1000)
            self.checkError([opt], 'expected one argument')
            self.checkError([opt, 'foo'], 'invalid int value')
