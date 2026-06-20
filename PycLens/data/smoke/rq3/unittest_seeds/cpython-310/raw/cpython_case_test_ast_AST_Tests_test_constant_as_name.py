# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_constant_as_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for constant in ('True', 'False', 'None'):
        expr = ast.Expression(ast.Name(constant, ast.Load()))
        ast.fix_missing_locations(expr)
        with self.assertRaisesRegex(ValueError, f"identifier field can't represent '{constant}' constant"):
            compile(expr, '<test>', 'eval')
