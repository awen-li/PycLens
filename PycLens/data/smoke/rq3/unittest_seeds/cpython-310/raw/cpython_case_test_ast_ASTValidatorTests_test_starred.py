# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_starred

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    left = ast.List([ast.Starred(ast.Name('x', ast.Load()), ast.Store())], ast.Store())
    assign = ast.Assign([left], ast.Num(4))
    self.stmt(assign, 'must have Store context')
