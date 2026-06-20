# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_invalid_syntax_errors_async

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check_syntax_error(self, 'async def f(a, b = 5, /, c): pass', 'non-default argument follows default argument')
    check_syntax_error(self, 'async def f(a = 5, b, /, c): pass', 'non-default argument follows default argument')
    check_syntax_error(self, 'async def f(a = 5, b=1, /, c, d=2): pass', 'non-default argument follows default argument')
    check_syntax_error(self, 'async def f(a = 5, b, /): pass', 'non-default argument follows default argument')
    check_syntax_error(self, 'async def f(*args, /): pass')
    check_syntax_error(self, 'async def f(*args, a, /): pass')
    check_syntax_error(self, 'async def f(**kwargs, /): pass')
    check_syntax_error(self, 'async def f(/, a = 1): pass')
    check_syntax_error(self, 'async def f(/, a): pass')
    check_syntax_error(self, 'async def f(/): pass')
    check_syntax_error(self, 'async def f(*, a, /): pass')
    check_syntax_error(self, 'async def f(*, /, a): pass')
    check_syntax_error(self, 'async def f(a, /, a): pass', "duplicate argument 'a' in function definition")
    check_syntax_error(self, 'async def f(a, /, *, a): pass', "duplicate argument 'a' in function definition")
    check_syntax_error(self, 'async def f(a, b/2, c): pass')
    check_syntax_error(self, 'async def f(a, /, c, /): pass')
    check_syntax_error(self, 'async def f(a, /, c, /, d): pass')
    check_syntax_error(self, 'async def f(a, /, c, /, d, *, e): pass')
    check_syntax_error(self, 'async def f(a, *, c, /, d, e): pass')
