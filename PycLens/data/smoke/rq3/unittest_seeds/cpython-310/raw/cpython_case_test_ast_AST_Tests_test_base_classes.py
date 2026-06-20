# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_base_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(ast.For, ast.stmt))
    self.assertTrue(issubclass(ast.Name, ast.expr))
    self.assertTrue(issubclass(ast.stmt, ast.AST))
    self.assertTrue(issubclass(ast.expr, ast.AST))
    self.assertTrue(issubclass(ast.comprehension, ast.AST))
    self.assertTrue(issubclass(ast.Gt, ast.AST))
