# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_variable_reuse_in_comprehensions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rebinding = '[x := i for i in range(3) if (x := i) or not x]'
    filter_ref = '[x := i for i in range(3) if x or not x]'
    body_ref = '[x for i in range(3) if (x := i) or not x]'
    nested_ref = '[j for i in range(3) if x or not x for j in range(3) if (x := i)][:-3]'
    cases = [('Rebind global', f'x = 1; result = {rebinding}'), ('Rebind nonlocal', f'result, x = (lambda x=1: ({rebinding}, x))()'), ('Filter global', f'x = 1; result = {filter_ref}'), ('Filter nonlocal', f'result, x = (lambda x=1: ({filter_ref}, x))()'), ('Body global', f'x = 1; result = {body_ref}'), ('Body nonlocal', f'result, x = (lambda x=1: ({body_ref}, x))()'), ('Nested global', f'x = 1; result = {nested_ref}'), ('Nested nonlocal', f'result, x = (lambda x=1: ({nested_ref}, x))()')]
    for (case, code) in cases:
        with self.subTest(case=case):
            ns = {}
            exec(code, ns)
            self.assertEqual(ns['x'], 2)
            self.assertEqual(ns['result'], [0, 1, 2])
