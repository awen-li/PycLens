# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_nonlocal_scope

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sentinel = object()

    def f():
        nonlocal_var = None

        def g():
            nonlocal nonlocal_var
            [(nonlocal_var := sentinel) for _ in range(1)]
        g()
        self.assertEqual(nonlocal_var, sentinel)
    f()
