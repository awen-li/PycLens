# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_long_option__partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = libregrtest._parse_args(['--qui'])
    self.assertTrue(ns.quiet)
    self.assertEqual(ns.verbose, 0)
