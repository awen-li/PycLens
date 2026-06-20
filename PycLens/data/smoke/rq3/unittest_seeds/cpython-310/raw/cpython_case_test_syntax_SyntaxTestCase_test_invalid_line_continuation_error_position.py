# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_invalid_line_continuation_error_position

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_error('a = 3 \\ 4', 'unexpected character after line continuation character', lineno=1, offset=8)
    self._check_error('1,\\#\n2', 'unexpected character after line continuation character', lineno=1, offset=4)
    self._check_error('\nfgdfgf\n1,\\#\n2\n', 'unexpected character after line continuation character', lineno=3, offset=4)
