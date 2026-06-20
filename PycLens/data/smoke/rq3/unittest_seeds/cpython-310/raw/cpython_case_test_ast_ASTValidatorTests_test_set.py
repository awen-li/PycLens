# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.expr(ast.Set([None]), 'None disallowed')
    s = ast.Set([ast.Name('x', ast.Store())])
    self.expr(s, 'must have Load context')
