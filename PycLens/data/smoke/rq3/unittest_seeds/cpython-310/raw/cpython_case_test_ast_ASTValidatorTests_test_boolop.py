# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_boolop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = ast.BoolOp(ast.And(), [])
    self.expr(b, 'less than 2 values')
    b = ast.BoolOp(ast.And(), [ast.Num(3)])
    self.expr(b, 'less than 2 values')
    b = ast.BoolOp(ast.And(), [ast.Num(4), None])
    self.expr(b, 'None disallowed')
    b = ast.BoolOp(ast.And(), [ast.Num(4), ast.Name('x', ast.Store())])
    self.expr(b, 'must have Load context')
