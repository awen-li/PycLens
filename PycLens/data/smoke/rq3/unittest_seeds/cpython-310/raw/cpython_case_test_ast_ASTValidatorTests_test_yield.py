# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_yield

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.expr(ast.Yield(ast.Name('x', ast.Store())), 'must have Load')
    self.expr(ast.YieldFrom(ast.Name('x', ast.Store())), 'must have Load')
