# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_assert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.stmt(ast.Assert(ast.Name('x', ast.Store()), None), 'must have Load context')
    assrt = ast.Assert(ast.Name('x', ast.Load()), ast.Name('y', ast.Store()))
    self.stmt(assrt, 'must have Load context')
