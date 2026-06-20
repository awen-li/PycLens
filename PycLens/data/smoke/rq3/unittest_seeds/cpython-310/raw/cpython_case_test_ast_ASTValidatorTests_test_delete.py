# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_delete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.stmt(ast.Delete([]), 'empty targets on Delete')
    self.stmt(ast.Delete([None]), 'None disallowed')
    self.stmt(ast.Delete([ast.Name('x', ast.Load())]), 'must have Del context')
