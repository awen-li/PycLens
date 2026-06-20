# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_augassign

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    aug = ast.AugAssign(ast.Name('x', ast.Load()), ast.Add(), ast.Name('y', ast.Load()))
    self.stmt(aug, 'must have Store context')
    aug = ast.AugAssign(ast.Name('x', ast.Store()), ast.Add(), ast.Name('y', ast.Store()))
    self.stmt(aug, 'must have Load context')
