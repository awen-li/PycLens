# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-i', '--ignore'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, 'pattern'])
            self.assertEqual(ns.ignore_tests, ['pattern'])
            self.checkError([opt], 'expected one argument')
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'w') as fp:
        print('matchfile1', file=fp)
        print('matchfile2', file=fp)
    filename = os.path.abspath(os_helper.TESTFN)
    ns = libregrtest._parse_args(['-m', 'match', '--ignorefile', filename])
    self.assertEqual(ns.ignore_tests, ['matchfile1', 'matchfile2'])
