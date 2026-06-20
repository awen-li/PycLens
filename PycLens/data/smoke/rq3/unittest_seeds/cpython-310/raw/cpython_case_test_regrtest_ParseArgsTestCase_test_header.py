# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = libregrtest._parse_args(['--header'])
    self.assertTrue(ns.header)
    ns = libregrtest._parse_args(['--verbose'])
    self.assertTrue(ns.header)
