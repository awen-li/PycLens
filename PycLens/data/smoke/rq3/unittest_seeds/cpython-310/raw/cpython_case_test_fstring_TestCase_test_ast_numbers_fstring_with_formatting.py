# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_ast_numbers_fstring_with_formatting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = ast.parse('f"Here is that pesky {xxx:.3f} again"')
    self.assertEqual(len(t.body), 1)
    self.assertEqual(t.body[0].lineno, 1)
    self.assertEqual(type(t.body[0]), ast.Expr)
    self.assertEqual(type(t.body[0].value), ast.JoinedStr)
    self.assertEqual(len(t.body[0].value.values), 3)
    self.assertEqual(type(t.body[0].value.values[0]), ast.Constant)
    self.assertEqual(type(t.body[0].value.values[1]), ast.FormattedValue)
    self.assertEqual(type(t.body[0].value.values[2]), ast.Constant)
    (_, expr, _) = t.body[0].value.values
    name = expr.value
    self.assertEqual(type(name), ast.Name)
    self.assertEqual(name.lineno, 1)
    self.assertEqual(name.end_lineno, 1)
    self.assertEqual(name.col_offset, 22)
    self.assertEqual(name.end_col_offset, 25)
