# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_while

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.stmt(ast.While(ast.Num(3), [], []), 'empty body on While')
    self.stmt(ast.While(ast.Name('x', ast.Store()), [ast.Pass()], []), 'must have Load context')
    self.stmt(ast.While(ast.Num(3), [ast.Pass()], [ast.Expr(ast.Name('x', ast.Store()))]), 'must have Load context')
