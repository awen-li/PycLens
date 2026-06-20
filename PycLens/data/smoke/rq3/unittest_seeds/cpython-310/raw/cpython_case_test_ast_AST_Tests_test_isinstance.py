# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_isinstance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(isinstance(ast.Num(42), ast.Num))
    self.assertTrue(isinstance(ast.Num(4.2), ast.Num))
    self.assertTrue(isinstance(ast.Num(4.2j), ast.Num))
    self.assertTrue(isinstance(ast.Str('42'), ast.Str))
    self.assertTrue(isinstance(ast.Bytes(b'42'), ast.Bytes))
    self.assertTrue(isinstance(ast.NameConstant(True), ast.NameConstant))
    self.assertTrue(isinstance(ast.NameConstant(False), ast.NameConstant))
    self.assertTrue(isinstance(ast.NameConstant(None), ast.NameConstant))
    self.assertTrue(isinstance(ast.Ellipsis(), ast.Ellipsis))
    self.assertTrue(isinstance(ast.Constant(42), ast.Num))
    self.assertTrue(isinstance(ast.Constant(4.2), ast.Num))
    self.assertTrue(isinstance(ast.Constant(4.2j), ast.Num))
    self.assertTrue(isinstance(ast.Constant('42'), ast.Str))
    self.assertTrue(isinstance(ast.Constant(b'42'), ast.Bytes))
    self.assertTrue(isinstance(ast.Constant(True), ast.NameConstant))
    self.assertTrue(isinstance(ast.Constant(False), ast.NameConstant))
    self.assertTrue(isinstance(ast.Constant(None), ast.NameConstant))
    self.assertTrue(isinstance(ast.Constant(...), ast.Ellipsis))
    self.assertFalse(isinstance(ast.Str('42'), ast.Num))
    self.assertFalse(isinstance(ast.Num(42), ast.Str))
    self.assertFalse(isinstance(ast.Str('42'), ast.Bytes))
    self.assertFalse(isinstance(ast.Num(42), ast.NameConstant))
    self.assertFalse(isinstance(ast.Num(42), ast.Ellipsis))
    self.assertFalse(isinstance(ast.NameConstant(True), ast.Num))
    self.assertFalse(isinstance(ast.NameConstant(False), ast.Num))
    self.assertFalse(isinstance(ast.Constant('42'), ast.Num))
    self.assertFalse(isinstance(ast.Constant(42), ast.Str))
    self.assertFalse(isinstance(ast.Constant('42'), ast.Bytes))
    self.assertFalse(isinstance(ast.Constant(42), ast.NameConstant))
    self.assertFalse(isinstance(ast.Constant(42), ast.Ellipsis))
    self.assertFalse(isinstance(ast.Constant(True), ast.Num))
    self.assertFalse(isinstance(ast.Constant(False), ast.Num))
    self.assertFalse(isinstance(ast.Constant(), ast.Num))
    self.assertFalse(isinstance(ast.Constant(), ast.Str))
    self.assertFalse(isinstance(ast.Constant(), ast.Bytes))
    self.assertFalse(isinstance(ast.Constant(), ast.NameConstant))
    self.assertFalse(isinstance(ast.Constant(), ast.Ellipsis))

    class S(str):
        pass
    self.assertTrue(isinstance(ast.Constant(S('42')), ast.Str))
    self.assertFalse(isinstance(ast.Constant(S('42')), ast.Num))
