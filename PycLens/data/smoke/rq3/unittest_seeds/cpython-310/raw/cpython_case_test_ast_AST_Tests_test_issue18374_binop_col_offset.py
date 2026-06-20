# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_issue18374_binop_col_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ast.parse('4+5+6+7')
    parent_binop = tree.body[0].value
    child_binop = parent_binop.left
    grandchild_binop = child_binop.left
    self.assertEqual(parent_binop.col_offset, 0)
    self.assertEqual(parent_binop.end_col_offset, 7)
    self.assertEqual(child_binop.col_offset, 0)
    self.assertEqual(child_binop.end_col_offset, 5)
    self.assertEqual(grandchild_binop.col_offset, 0)
    self.assertEqual(grandchild_binop.end_col_offset, 3)
    tree = ast.parse('4+5-\\\n 6-7')
    parent_binop = tree.body[0].value
    child_binop = parent_binop.left
    grandchild_binop = child_binop.left
    self.assertEqual(parent_binop.col_offset, 0)
    self.assertEqual(parent_binop.lineno, 1)
    self.assertEqual(parent_binop.end_col_offset, 4)
    self.assertEqual(parent_binop.end_lineno, 2)
    self.assertEqual(child_binop.col_offset, 0)
    self.assertEqual(child_binop.lineno, 1)
    self.assertEqual(child_binop.end_col_offset, 2)
    self.assertEqual(child_binop.end_lineno, 2)
    self.assertEqual(grandchild_binop.col_offset, 0)
    self.assertEqual(grandchild_binop.lineno, 1)
    self.assertEqual(grandchild_binop.end_col_offset, 3)
    self.assertEqual(grandchild_binop.end_lineno, 1)
