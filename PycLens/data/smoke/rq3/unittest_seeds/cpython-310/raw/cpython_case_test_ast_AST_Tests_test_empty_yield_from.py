# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_empty_yield_from

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    empty_yield_from = ast.parse('def f():\n yield from g()')
    empty_yield_from.body[0].body[0].value.value = None
    with self.assertRaises(ValueError) as cm:
        compile(empty_yield_from, '<test>', 'exec')
    self.assertIn("field 'value' is required", str(cm.exception))
