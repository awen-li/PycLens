# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    func = ast.Name('x', ast.Load())
    args = [ast.Name('y', ast.Load())]
    keywords = [ast.keyword('w', ast.Name('z', ast.Load()))]
    call = ast.Call(ast.Name('x', ast.Store()), args, keywords)
    self.expr(call, 'must have Load context')
    call = ast.Call(func, [None], keywords)
    self.expr(call, 'None disallowed')
    bad_keywords = [ast.keyword('w', ast.Name('z', ast.Store()))]
    call = ast.Call(func, args, bad_keywords)
    self.expr(call, 'must have Load context')
