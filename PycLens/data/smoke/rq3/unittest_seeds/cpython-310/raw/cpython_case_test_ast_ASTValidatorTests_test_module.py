# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = ast.Interactive([ast.Expr(ast.Name('x', ast.Store()))])
    self.mod(m, 'must have Load context', 'single')
    m = ast.Expression(ast.Name('x', ast.Store()))
    self.mod(m, 'must have Load context', 'eval')
