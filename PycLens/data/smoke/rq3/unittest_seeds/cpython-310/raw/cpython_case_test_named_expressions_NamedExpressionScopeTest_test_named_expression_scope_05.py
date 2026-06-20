# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_05

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(a):
        return a
    input_data = [1, 2, 3]
    res = [(x, y, x / y) for x in input_data if (y := spam(x)) > 0]
    self.assertEqual(res, [(1, 1, 1.0), (2, 2, 1.0), (3, 3, 1.0)])
    self.assertEqual(y, 3)
