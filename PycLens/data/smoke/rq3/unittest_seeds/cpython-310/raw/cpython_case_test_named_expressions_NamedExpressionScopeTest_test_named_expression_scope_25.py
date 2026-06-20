# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_named_expressions.py
# case: NamedExpressionScopeTest_test_named_expression_scope_25

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {}
    code = 'a = 10\ndef spam():\n    global a\n    (a := 20)\nspam()'
    exec(code, ns, {})
    self.assertEqual(ns['a'], 20)
