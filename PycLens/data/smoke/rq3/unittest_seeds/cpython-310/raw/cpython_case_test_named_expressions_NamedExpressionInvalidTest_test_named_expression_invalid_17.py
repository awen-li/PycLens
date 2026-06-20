# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionInvalidTest_test_named_expression_invalid_17

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '[i := 0, j := 1 for i, j in [(1, 2), (3, 4)]]'
    with self.assertRaisesRegex(SyntaxError, 'did you forget parentheses around the comprehension target?'):
        exec(code, {}, {})
