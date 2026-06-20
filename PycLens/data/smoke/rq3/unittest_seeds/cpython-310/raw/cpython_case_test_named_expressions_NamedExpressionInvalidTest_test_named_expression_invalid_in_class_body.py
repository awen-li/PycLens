# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionInvalidTest_test_named_expression_invalid_in_class_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'class Foo():\n            [(42, 1 + ((( j := i )))) for i in range(5)]\n        '
    with self.assertRaisesRegex(SyntaxError, 'assignment expression within a comprehension cannot be used in a class body'):
        exec(code, {}, {})
