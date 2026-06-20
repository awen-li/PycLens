# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_raise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = ast.Raise(None, ast.Num(3))
    self.stmt(r, 'Raise with cause but no exception')
    r = ast.Raise(ast.Name('x', ast.Store()), None)
    self.stmt(r, 'must have Load context')
    r = ast.Raise(ast.Num(4), ast.Name('x', ast.Store()))
    self.stmt(r, 'must have Load context')
