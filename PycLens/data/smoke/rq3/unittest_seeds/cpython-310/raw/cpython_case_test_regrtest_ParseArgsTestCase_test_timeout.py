# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ParseArgsTestCase_test_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = libregrtest._parse_args(['--timeout', '4.2'])
    self.assertEqual(ns.timeout, 4.2)
    self.checkError(['--timeout'], 'expected one argument')
    self.checkError(['--timeout', 'foo'], 'invalid float value')
