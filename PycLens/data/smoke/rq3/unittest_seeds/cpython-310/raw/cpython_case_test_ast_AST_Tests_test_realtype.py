# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_realtype

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(type(ast.Num(42)), ast.Constant)
    self.assertEqual(type(ast.Num(4.25)), ast.Constant)
    self.assertEqual(type(ast.Num(4.25j)), ast.Constant)
    self.assertEqual(type(ast.Str('42')), ast.Constant)
    self.assertEqual(type(ast.Bytes(b'42')), ast.Constant)
    self.assertEqual(type(ast.NameConstant(True)), ast.Constant)
    self.assertEqual(type(ast.NameConstant(False)), ast.Constant)
    self.assertEqual(type(ast.NameConstant(None)), ast.Constant)
    self.assertEqual(type(ast.Ellipsis()), ast.Constant)
