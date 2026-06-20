# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-m', '--match'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, 'pattern'])
            self.assertEqual(ns.match_tests, ['pattern'])
            self.checkError([opt], 'expected one argument')
    ns = libregrtest._parse_args(['-m', 'pattern1', '-m', 'pattern2'])
    self.assertEqual(ns.match_tests, ['pattern1', 'pattern2'])
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'w') as fp:
        print('matchfile1', file=fp)
        print('matchfile2', file=fp)
    filename = os.path.abspath(os_helper.TESTFN)
    ns = libregrtest._parse_args(['-m', 'match', '--matchfile', filename])
    self.assertEqual(ns.match_tests, ['match', 'matchfile1', 'matchfile2'])
