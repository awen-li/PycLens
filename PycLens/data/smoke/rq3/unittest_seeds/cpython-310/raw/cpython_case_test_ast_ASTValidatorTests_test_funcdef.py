# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_funcdef

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ast.arguments([], [], None, [], [], None, [])
    f = ast.FunctionDef('x', a, [], [], None)
    self.stmt(f, 'empty body on FunctionDef')
    f = ast.FunctionDef('x', a, [ast.Pass()], [ast.Name('x', ast.Store())], None)
    self.stmt(f, 'must have Load context')
    f = ast.FunctionDef('x', a, [ast.Pass()], [], ast.Name('x', ast.Store()))
    self.stmt(f, 'must have Load context')

    def fac(args):
        return ast.FunctionDef('x', args, [ast.Pass()], [], None)
    self._check_arguments(fac, self.stmt)
