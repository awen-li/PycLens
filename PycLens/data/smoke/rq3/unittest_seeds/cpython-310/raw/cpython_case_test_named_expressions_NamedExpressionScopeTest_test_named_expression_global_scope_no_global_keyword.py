# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_global_scope_no_global_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sentinel = object()

    def f():
        GLOBAL_VAR = None
        [(GLOBAL_VAR := sentinel) for _ in range(1)]
        self.assertEqual(GLOBAL_VAR, sentinel)
    f()
    self.assertEqual(GLOBAL_VAR, None)
