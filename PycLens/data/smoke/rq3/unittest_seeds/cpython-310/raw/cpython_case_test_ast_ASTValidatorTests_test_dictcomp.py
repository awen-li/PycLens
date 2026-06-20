# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_dictcomp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = ast.comprehension(ast.Name('y', ast.Store()), ast.Name('p', ast.Load()), [], 0)
    c = ast.DictComp(ast.Name('x', ast.Store()), ast.Name('y', ast.Load()), [g])
    self.expr(c, 'must have Load context')
    c = ast.DictComp(ast.Name('x', ast.Load()), ast.Name('y', ast.Store()), [g])
    self.expr(c, 'must have Load context')

    def factory(comps):
        k = ast.Name('x', ast.Load())
        v = ast.Name('y', ast.Load())
        return ast.DictComp(k, v, comps)
    self._check_comprehension(factory)
