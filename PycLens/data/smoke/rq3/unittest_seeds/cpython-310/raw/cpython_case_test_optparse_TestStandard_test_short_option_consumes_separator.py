# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestStandard_test_short_option_consumes_separator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-a', '--', 'foo', 'bar'], {'a': '--', 'boo': None, 'foo': None}, ['foo', 'bar'])
    self.assertParseOK(['-a', '--', '--foo', 'bar'], {'a': '--', 'boo': None, 'foo': ['bar']}, [])
