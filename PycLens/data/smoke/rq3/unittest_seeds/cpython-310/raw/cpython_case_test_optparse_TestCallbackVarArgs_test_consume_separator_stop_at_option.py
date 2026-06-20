# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestCallbackVarArgs_test_consume_separator_stop_at_option

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-c', '37', '--', 'xxx', '-b', 'hello'], {'a': None, 'b': True, 'c': ['37', '--', 'xxx']}, ['hello'])
