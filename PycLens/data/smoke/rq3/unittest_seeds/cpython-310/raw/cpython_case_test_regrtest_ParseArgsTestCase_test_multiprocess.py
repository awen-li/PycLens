# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_multiprocess

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-j', '--multiprocess'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, '2'])
            self.assertEqual(ns.use_mp, 2)
            self.checkError([opt], 'expected one argument')
            self.checkError([opt, 'foo'], 'invalid int value')
            self.checkError([opt, '2', '-T'], "don't go together")
            self.checkError([opt, '0', '-T'], "don't go together")
