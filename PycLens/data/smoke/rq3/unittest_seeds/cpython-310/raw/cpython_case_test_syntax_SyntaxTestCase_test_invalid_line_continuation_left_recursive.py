# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_invalid_line_continuation_left_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_error('A.Ɗ\\ ', 'unexpected character after line continuation character')
    self._check_error('A.μ\\\n', 'unexpected EOF while parsing')
