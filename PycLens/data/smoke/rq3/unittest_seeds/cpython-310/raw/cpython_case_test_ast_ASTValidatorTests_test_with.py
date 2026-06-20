# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_with

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = ast.Pass()
    self.stmt(ast.With([], [p]), 'empty items on With')
    i = ast.withitem(ast.Num(3), None)
    self.stmt(ast.With([i], []), 'empty body on With')
    i = ast.withitem(ast.Name('x', ast.Store()), None)
    self.stmt(ast.With([i], [p]), 'must have Load context')
    i = ast.withitem(ast.Num(3), ast.Name('x', ast.Load()))
    self.stmt(ast.With([i], [p]), 'must have Store context')
