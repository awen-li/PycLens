# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_ast_asdl_signature

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ast.withitem.__doc__, 'withitem(expr context_expr, expr? optional_vars)')
    self.assertEqual(ast.GtE.__doc__, 'GtE')
    self.assertEqual(ast.Name.__doc__, 'Name(identifier id, expr_context ctx)')
    self.assertEqual(ast.cmpop.__doc__, 'cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn')
    expressions = [f'     | {node.__doc__}' for node in ast.expr.__subclasses__()]
    expressions[0] = f'expr = {ast.expr.__subclasses__()[0].__doc__}'
    self.assertCountEqual(ast.expr.__doc__.split('\n'), expressions)
