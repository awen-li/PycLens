# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_if

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.stmt(ast.If(ast.Num(3), [], []), 'empty body on If')
    i = ast.If(ast.Name('x', ast.Store()), [ast.Pass()], [])
    self.stmt(i, 'must have Load context')
    i = ast.If(ast.Num(3), [ast.Expr(ast.Name('x', ast.Store()))], [])
    self.stmt(i, 'must have Load context')
    i = ast.If(ast.Num(3), [ast.Pass()], [ast.Expr(ast.Name('x', ast.Store()))])
    self.stmt(i, 'must have Load context')
