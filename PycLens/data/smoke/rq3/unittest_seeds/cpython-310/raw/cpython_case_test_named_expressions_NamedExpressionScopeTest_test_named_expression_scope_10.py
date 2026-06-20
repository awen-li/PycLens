# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_10

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = [(b := [(a := 1) for i in range(2)]) for j in range(2)]
    self.assertEqual(res, [[1, 1], [1, 1]])
    self.assertEqual(a, 1)
    self.assertEqual(b, [1, 1])
