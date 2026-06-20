# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_classdef

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cls(bases=None, keywords=None, body=None, decorator_list=None):
        if bases is None:
            bases = []
        if keywords is None:
            keywords = []
        if body is None:
            body = [ast.Pass()]
        if decorator_list is None:
            decorator_list = []
        return ast.ClassDef('myclass', bases, keywords, body, decorator_list)
    self.stmt(cls(bases=[ast.Name('x', ast.Store())]), 'must have Load context')
    self.stmt(cls(keywords=[ast.keyword('x', ast.Name('x', ast.Store()))]), 'must have Load context')
    self.stmt(cls(body=[]), 'empty body on ClassDef')
    self.stmt(cls(body=[None]), 'None disallowed')
    self.stmt(cls(decorator_list=[ast.Name('x', ast.Store())]), 'must have Load context')
