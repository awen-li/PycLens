# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = ast.Dict([], [ast.Name('x', ast.Load())])
    self.expr(d, 'same number of keys as values')
    d = ast.Dict([ast.Name('x', ast.Load())], [None])
    self.expr(d, 'None disallowed')
