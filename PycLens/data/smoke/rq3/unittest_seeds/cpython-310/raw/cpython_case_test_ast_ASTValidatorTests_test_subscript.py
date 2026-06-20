# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_subscript

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sub = ast.Subscript(ast.Name('x', ast.Store()), ast.Num(3), ast.Load())
    self.expr(sub, 'must have Load context')
    x = ast.Name('x', ast.Load())
    sub = ast.Subscript(x, ast.Name('y', ast.Store()), ast.Load())
    self.expr(sub, 'must have Load context')
    s = ast.Name('x', ast.Store())
    for args in ((s, None, None), (None, s, None), (None, None, s)):
        sl = ast.Slice(*args)
        self.expr(ast.Subscript(x, sl, ast.Load()), 'must have Load context')
    sl = ast.Tuple([], ast.Load())
    self.expr(ast.Subscript(x, sl, ast.Load()))
    sl = ast.Tuple([s], ast.Load())
    self.expr(ast.Subscript(x, sl, ast.Load()), 'must have Load context')
