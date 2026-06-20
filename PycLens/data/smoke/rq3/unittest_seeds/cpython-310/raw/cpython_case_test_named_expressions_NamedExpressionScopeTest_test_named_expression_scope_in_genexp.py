# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_in_genexp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 1
    b = [1, 2, 3, 4]
    genexp = ((c := (i + a)) for i in b)
    self.assertNotIn('c', locals())
    for (idx, elem) in enumerate(genexp):
        self.assertEqual(elem, b[idx] + a)
