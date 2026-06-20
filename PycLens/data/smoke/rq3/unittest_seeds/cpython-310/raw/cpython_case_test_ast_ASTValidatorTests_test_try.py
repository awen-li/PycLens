# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_try

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = ast.Pass()
    t = ast.Try([], [], [], [p])
    self.stmt(t, 'empty body on Try')
    t = ast.Try([ast.Expr(ast.Name('x', ast.Store()))], [], [], [p])
    self.stmt(t, 'must have Load context')
    t = ast.Try([p], [], [], [])
    self.stmt(t, 'Try has neither except handlers nor finalbody')
    t = ast.Try([p], [], [p], [p])
    self.stmt(t, 'Try has orelse but no except handlers')
    t = ast.Try([p], [ast.ExceptHandler(None, 'x', [])], [], [])
    self.stmt(t, 'empty body on ExceptHandler')
    e = [ast.ExceptHandler(ast.Name('x', ast.Store()), 'y', [p])]
    self.stmt(ast.Try([p], e, [], []), 'must have Load context')
    e = [ast.ExceptHandler(None, 'x', [p])]
    t = ast.Try([p], e, [ast.Expr(ast.Name('x', ast.Store()))], [p])
    self.stmt(t, 'must have Load context')
    t = ast.Try([p], e, [p], [ast.Expr(ast.Name('x', ast.Store()))])
    self.stmt(t, 'must have Load context')
