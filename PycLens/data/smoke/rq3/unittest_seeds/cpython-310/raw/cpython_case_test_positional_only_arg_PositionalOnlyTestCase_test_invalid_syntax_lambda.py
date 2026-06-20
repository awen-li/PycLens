# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_invalid_syntax_lambda

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check_syntax_error(self, 'lambda a, b = 5, /, c: None', 'non-default argument follows default argument')
    check_syntax_error(self, 'lambda a = 5, b, /, c: None', 'non-default argument follows default argument')
    check_syntax_error(self, 'lambda a = 5, b, /: None', 'non-default argument follows default argument')
    check_syntax_error(self, 'lambda *args, /: None')
    check_syntax_error(self, 'lambda *args, a, /: None')
    check_syntax_error(self, 'lambda **kwargs, /: None')
    check_syntax_error(self, 'lambda /, a = 1: None')
    check_syntax_error(self, 'lambda /, a: None')
    check_syntax_error(self, 'lambda /: None')
    check_syntax_error(self, 'lambda *, a, /: None')
    check_syntax_error(self, 'lambda *, /, a: None')
    check_syntax_error(self, 'lambda a, /, a: None', "duplicate argument 'a' in function definition")
    check_syntax_error(self, 'lambda a, /, *, a: None', "duplicate argument 'a' in function definition")
    check_syntax_error(self, 'lambda a, /, b, /: None')
    check_syntax_error(self, 'lambda a, /, b, /, c: None')
    check_syntax_error(self, 'lambda a, /, b, /, c, *, d: None')
    check_syntax_error(self, 'lambda a, *, b, /, c: None')
