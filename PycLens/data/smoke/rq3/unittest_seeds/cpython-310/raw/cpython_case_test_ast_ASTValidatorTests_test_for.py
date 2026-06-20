# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_for

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ast.Name('x', ast.Store())
    y = ast.Name('y', ast.Load())
    p = ast.Pass()
    self.stmt(ast.For(x, y, [], []), 'empty body on For')
    self.stmt(ast.For(ast.Name('x', ast.Load()), y, [p], []), 'must have Store context')
    self.stmt(ast.For(x, ast.Name('y', ast.Store()), [p], []), 'must have Load context')
    e = ast.Expr(ast.Name('x', ast.Store()))
    self.stmt(ast.For(x, y, [e], []), 'must have Load context')
    self.stmt(ast.For(x, y, [p], [e]), 'must have Load context')
