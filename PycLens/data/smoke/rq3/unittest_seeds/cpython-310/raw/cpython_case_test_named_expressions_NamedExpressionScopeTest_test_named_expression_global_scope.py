# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_global_scope

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sentinel = object()
    global GLOBAL_VAR

    def f():
        global GLOBAL_VAR
        [(GLOBAL_VAR := sentinel) for _ in range(1)]
        self.assertEqual(GLOBAL_VAR, sentinel)
    try:
        f()
        self.assertEqual(GLOBAL_VAR, sentinel)
    finally:
        GLOBAL_VAR = None
