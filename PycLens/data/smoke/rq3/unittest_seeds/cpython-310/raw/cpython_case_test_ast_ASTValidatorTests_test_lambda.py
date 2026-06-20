# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_lambda

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ast.arguments([], [], None, [], [], None, [])
    self.expr(ast.Lambda(a, ast.Name('x', ast.Store())), 'must have Load context')

    def fac(args):
        return ast.Lambda(args, ast.Name('x', ast.Load()))
    self._check_arguments(fac, self.expr)
