# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_02

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    total = 0
    partial_sums = [(total := (total + v)) for v in range(5)]
    self.assertEqual(partial_sums, [0, 1, 3, 6, 10])
    self.assertEqual(total, 10)
