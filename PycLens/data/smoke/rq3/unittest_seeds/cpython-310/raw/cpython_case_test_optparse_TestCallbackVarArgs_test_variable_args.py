# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestCallbackVarArgs_test_variable_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-a3', '-5', '--callback', 'foo', 'bar'], {'a': (3, -5), 'b': None, 'c': ['foo', 'bar']}, [])
