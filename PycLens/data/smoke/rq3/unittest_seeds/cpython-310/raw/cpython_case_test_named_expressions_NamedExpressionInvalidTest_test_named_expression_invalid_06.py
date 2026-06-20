# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionInvalidTest_test_named_expression_invalid_06

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '((a, b) := (1, 2))'
    with self.assertRaisesRegex(SyntaxError, 'cannot use assignment expressions with tuple'):
        exec(code, {}, {})
