# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_03

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    containsOne = any(((lastNum := num) == 1 for num in [1, 2, 3]))
    self.assertTrue(containsOne)
    self.assertEqual(lastNum, 1)
