# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_09

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def spam(a):
        return a

    def eggs(b):
        return b * 2
    res = [spam((a := eggs((a := h)))) for h in range(2)]
    self.assertEqual(res, [0, 2])
    self.assertEqual(a, 2)
