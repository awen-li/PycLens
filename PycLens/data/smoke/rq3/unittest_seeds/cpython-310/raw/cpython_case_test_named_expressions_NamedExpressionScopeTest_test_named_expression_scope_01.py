# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_01

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'def spam():\n    (a := 5)\nprint(a)'
    with self.assertRaisesRegex(NameError, "name 'a' is not defined"):
        exec(code, {}, {})
