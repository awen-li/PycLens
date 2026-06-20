# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_ast_line_numbers_with_parentheses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expr = '\nx = (\n    f" {test(t)}"\n)'
    t = ast.parse(expr)
    self.assertEqual(type(t), ast.Module)
    self.assertEqual(len(t.body), 1)
    call = t.body[0].value.values[1].value
    self.assertEqual(type(call), ast.Call)
    self.assertEqual(call.lineno, 3)
    self.assertEqual(call.end_lineno, 3)
    self.assertEqual(call.col_offset, 8)
    self.assertEqual(call.end_col_offset, 15)
    expr = "\nx = (\n        'PERL_MM_OPT', (\n            f'wat'\n            f'some_string={f(x)} '\n            f'wat'\n        ),\n)\n"
    t = ast.parse(expr)
    self.assertEqual(type(t), ast.Module)
    self.assertEqual(len(t.body), 1)
    fstring = t.body[0].value.elts[1]
    self.assertEqual(type(fstring), ast.JoinedStr)
    self.assertEqual(len(fstring.values), 3)
    (wat1, middle, wat2) = fstring.values
    self.assertEqual(type(wat1), ast.Constant)
    self.assertEqual(wat1.lineno, 4)
    self.assertEqual(wat1.end_lineno, 6)
    self.assertEqual(wat1.col_offset, 12)
    self.assertEqual(wat1.end_col_offset, 18)
    call = middle.value
    self.assertEqual(type(call), ast.Call)
    self.assertEqual(call.lineno, 5)
    self.assertEqual(call.end_lineno, 5)
    self.assertEqual(call.col_offset, 27)
    self.assertEqual(call.end_col_offset, 31)
    self.assertEqual(type(wat2), ast.Constant)
    self.assertEqual(wat2.lineno, 4)
    self.assertEqual(wat2.end_lineno, 6)
    self.assertEqual(wat2.col_offset, 12)
    self.assertEqual(wat2.end_col_offset, 18)
