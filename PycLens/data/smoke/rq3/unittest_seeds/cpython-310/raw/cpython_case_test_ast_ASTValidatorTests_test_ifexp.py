# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_ifexp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = ast.Name('x', ast.Load())
    s = ast.Name('y', ast.Store())
    for args in ((s, l, l), (l, s, l), (l, l, s)):
        self.expr(ast.IfExp(*args), 'must have Load context')
