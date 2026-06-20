# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_ast_line_numbers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expr = "\na = 10\nf'{a * x()}'"
    t = ast.parse(expr)
    self.assertEqual(type(t), ast.Module)
    self.assertEqual(len(t.body), 2)
    self.assertEqual(type(t.body[0]), ast.Assign)
    self.assertEqual(t.body[0].lineno, 2)
    self.assertEqual(type(t.body[1]), ast.Expr)
    self.assertEqual(type(t.body[1].value), ast.JoinedStr)
    self.assertEqual(len(t.body[1].value.values), 1)
    self.assertEqual(type(t.body[1].value.values[0]), ast.FormattedValue)
    self.assertEqual(t.body[1].lineno, 3)
    self.assertEqual(t.body[1].value.lineno, 3)
    self.assertEqual(t.body[1].value.values[0].lineno, 3)
    binop = t.body[1].value.values[0].value
    self.assertEqual(type(binop), ast.BinOp)
    self.assertEqual(type(binop.left), ast.Name)
    self.assertEqual(type(binop.op), ast.Mult)
    self.assertEqual(type(binop.right), ast.Call)
    self.assertEqual(binop.lineno, 3)
    self.assertEqual(binop.left.lineno, 3)
    self.assertEqual(binop.right.lineno, 3)
    self.assertEqual(binop.col_offset, 3)
    self.assertEqual(binop.left.col_offset, 3)
    self.assertEqual(binop.right.col_offset, 7)
