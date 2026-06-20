# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_randseed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = libregrtest._parse_args(['--randseed', '12345'])
    self.assertEqual(ns.random_seed, 12345)
    self.assertTrue(ns.randomize)
    self.checkError(['--randseed'], 'expected one argument')
    self.checkError(['--randseed', 'foo'], 'invalid int value')
