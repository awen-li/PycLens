# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_use

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opt in ('-u', '--use'):
        with self.subTest(opt=opt):
            ns = libregrtest._parse_args([opt, 'gui,network'])
            self.assertEqual(ns.use_resources, ['gui', 'network'])
            ns = libregrtest._parse_args([opt, 'gui,none,network'])
            self.assertEqual(ns.use_resources, ['network'])
            expected = list(libregrtest.ALL_RESOURCES)
            expected.remove('gui')
            ns = libregrtest._parse_args([opt, 'all,-gui'])
            self.assertEqual(ns.use_resources, expected)
            self.checkError([opt], 'expected one argument')
            self.checkError([opt, 'foo'], 'invalid resource')
            ns = libregrtest._parse_args([opt, 'all,tzdata'])
            self.assertEqual(ns.use_resources, list(libregrtest.ALL_RESOURCES) + ['tzdata'])
            ns = libregrtest._parse_args([opt, 'extralargefile'])
            self.assertEqual(ns.use_resources, ['extralargefile'])
