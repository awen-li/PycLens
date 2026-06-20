# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestMultipleArgsAppend_test_nargs_append_const

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertParseOK(['--zero', '--foo', '3', '4', '-z'], {'point': None, 'foo': [(0, 0), (3, 4), (0, 0)]}, [])
