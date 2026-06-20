# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_huntrleaks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-R', '--huntrleaks'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, ':'])
            self.assertEqual(ns.huntrleaks, (5, 4, 'reflog.txt'))
            ns = libregrtest._parse_args([opt, '6:'])
            self.assertEqual(ns.huntrleaks, (6, 4, 'reflog.txt'))
            ns = libregrtest._parse_args([opt, ':3'])
            self.assertEqual(ns.huntrleaks, (5, 3, 'reflog.txt'))
            ns = libregrtest._parse_args([opt, '6:3:leaks.log'])
            self.assertEqual(ns.huntrleaks, (6, 3, 'leaks.log'))
            self.checkError([opt], 'expected one argument')
            self.checkError([opt, '6'], 'needs 2 or 3 colon-separated arguments')
            self.checkError([opt, 'foo:'], 'invalid huntrleaks value')
            self.checkError([opt, '6:foo'], 'invalid huntrleaks value')
