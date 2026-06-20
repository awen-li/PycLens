# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestMultipleArgsAppend_test_nargs_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['-f', '4', '-3', 'blah', '--foo', '1', '666'], {'point': None, 'foo': [(4, -3), (1, 666)]}, ['blah'])
