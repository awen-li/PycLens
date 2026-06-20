# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_parse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ast.parse('foo(1 + 1)')
    b = compile('foo(1 + 1)', '<unknown>', 'exec', ast.PyCF_ONLY_AST)
    self.assertEqual(ast.dump(a), ast.dump(b))
