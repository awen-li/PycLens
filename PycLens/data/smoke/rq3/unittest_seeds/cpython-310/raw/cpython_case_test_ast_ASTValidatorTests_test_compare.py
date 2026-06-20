# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    left = ast.Name('x', ast.Load())
    comp = ast.Compare(left, [ast.In()], [])
    self.expr(comp, 'no comparators')
    comp = ast.Compare(left, [ast.In()], [ast.Num(4), ast.Num(5)])
    self.expr(comp, 'different number of comparators and operands')
    comp = ast.Compare(ast.Num('blah'), [ast.In()], [left])
    self.expr(comp)
    comp = ast.Compare(left, [ast.In()], [ast.Num('blah')])
    self.expr(comp)
