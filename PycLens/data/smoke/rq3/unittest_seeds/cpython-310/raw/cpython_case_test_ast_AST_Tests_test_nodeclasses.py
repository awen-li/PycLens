# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_nodeclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ast.BinOp()
    self.assertEqual(x._fields, ('left', 'op', 'right'))
    x.foobarbaz = 5
    self.assertEqual(x.foobarbaz, 5)
    n1 = ast.Num(1)
    n3 = ast.Num(3)
    addop = ast.Add()
    x = ast.BinOp(n1, addop, n3)
    self.assertEqual(x.left, n1)
    self.assertEqual(x.op, addop)
    self.assertEqual(x.right, n3)
    x = ast.BinOp(1, 2, 3)
    self.assertEqual(x.left, 1)
    self.assertEqual(x.op, 2)
    self.assertEqual(x.right, 3)
    x = ast.BinOp(1, 2, 3, lineno=0)
    self.assertEqual(x.left, 1)
    self.assertEqual(x.op, 2)
    self.assertEqual(x.right, 3)
    self.assertEqual(x.lineno, 0)
    self.assertRaises(TypeError, ast.BinOp, 1, 2, 3, 4)
    self.assertRaises(TypeError, ast.BinOp, 1, 2, 3, 4, lineno=0)
    x = ast.BinOp(left=1, op=2, right=3, lineno=0)
    self.assertEqual(x.left, 1)
    self.assertEqual(x.op, 2)
    self.assertEqual(x.right, 3)
    self.assertEqual(x.lineno, 0)
    x = ast.BinOp(1, 2, 3, foobarbaz=42)
    self.assertEqual(x.foobarbaz, 42)
