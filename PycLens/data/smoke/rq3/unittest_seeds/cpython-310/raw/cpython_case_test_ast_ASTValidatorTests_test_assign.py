# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_assign

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.stmt(ast.Assign([], ast.Num(3)), 'empty targets on Assign')
    self.stmt(ast.Assign([None], ast.Num(3)), 'None disallowed')
    self.stmt(ast.Assign([ast.Name('x', ast.Load())], ast.Num(3)), 'must have Store context')
    self.stmt(ast.Assign([ast.Name('x', ast.Store())], ast.Name('y', ast.Store())), 'must have Load context')
