# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_importfrom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    imp = ast.ImportFrom(None, [ast.alias('x', None)], -42)
    self.stmt(imp, 'Negative ImportFrom level')
    self.stmt(ast.ImportFrom(None, [], 0), 'empty names on ImportFrom')
