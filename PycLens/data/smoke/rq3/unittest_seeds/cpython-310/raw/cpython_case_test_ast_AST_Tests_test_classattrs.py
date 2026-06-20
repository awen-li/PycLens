# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_classattrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ast.Num()
    self.assertEqual(x._fields, ('value', 'kind'))
    with self.assertRaises(AttributeError):
        x.value
    with self.assertRaises(AttributeError):
        x.n
    x = ast.Num(42)
    self.assertEqual(x.value, 42)
    self.assertEqual(x.n, 42)
    with self.assertRaises(AttributeError):
        x.lineno
    with self.assertRaises(AttributeError):
        x.foobar
    x = ast.Num(lineno=2)
    self.assertEqual(x.lineno, 2)
    x = ast.Num(42, lineno=0)
    self.assertEqual(x.lineno, 0)
    self.assertEqual(x._fields, ('value', 'kind'))
    self.assertEqual(x.value, 42)
    self.assertEqual(x.n, 42)
    self.assertRaises(TypeError, ast.Num, 1, None, 2)
    self.assertRaises(TypeError, ast.Num, 1, None, 2, lineno=0)
    self.assertEqual(ast.Constant(1, foo='bar').foo, 'bar')
    self.assertEqual(ast.Num(1, foo='bar').foo, 'bar')
    with self.assertRaisesRegex(TypeError, "Num got multiple values for argument 'n'"):
        ast.Num(1, n=2)
    with self.assertRaisesRegex(TypeError, "Constant got multiple values for argument 'value'"):
        ast.Constant(1, value=2)
    self.assertEqual(ast.Num(42).n, 42)
    self.assertEqual(ast.Num(4.25).n, 4.25)
    self.assertEqual(ast.Num(4.25j).n, 4.25j)
    self.assertEqual(ast.Str('42').s, '42')
    self.assertEqual(ast.Bytes(b'42').s, b'42')
    self.assertIs(ast.NameConstant(True).value, True)
    self.assertIs(ast.NameConstant(False).value, False)
    self.assertIs(ast.NameConstant(None).value, None)
    self.assertEqual(ast.Constant(42).value, 42)
    self.assertEqual(ast.Constant(4.25).value, 4.25)
    self.assertEqual(ast.Constant(4.25j).value, 4.25j)
    self.assertEqual(ast.Constant('42').value, '42')
    self.assertEqual(ast.Constant(b'42').value, b'42')
    self.assertIs(ast.Constant(True).value, True)
    self.assertIs(ast.Constant(False).value, False)
    self.assertIs(ast.Constant(None).value, None)
    self.assertIs(ast.Constant(...).value, ...)
