# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_generator_in_function_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_error('foo(x,    y for y in range(3) for z in range(2) if z    , p)', 'Generator expression must be parenthesized', lineno=1, end_lineno=1, offset=11, end_offset=53)
