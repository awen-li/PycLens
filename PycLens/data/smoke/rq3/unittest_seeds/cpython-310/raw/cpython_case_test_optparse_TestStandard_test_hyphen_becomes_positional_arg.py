# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestStandard_test_hyphen_becomes_positional_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-ab', '-', '--foo', 'bar'], {'a': 'b', 'boo': None, 'foo': ['bar']}, ['-'])
