# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_17

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = 0
    res = [(b := (i + b)) for i in range(5)]
    self.assertEqual(res, [0, 1, 3, 6, 10])
    self.assertEqual(b, 10)
