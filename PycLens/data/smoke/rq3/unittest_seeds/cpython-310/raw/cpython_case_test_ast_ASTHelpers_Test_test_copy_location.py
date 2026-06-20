# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_copy_location

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = ast.parse('1 + 1', mode='eval')
    src.body.right = ast.copy_location(ast.Num(2), src.body.right)
    self.assertEqual(ast.dump(src, include_attributes=True), 'Expression(body=BinOp(left=Constant(value=1, lineno=1, col_offset=0, end_lineno=1, end_col_offset=1), op=Add(), right=Constant(value=2, lineno=1, col_offset=4, end_lineno=1, end_col_offset=5), lineno=1, col_offset=0, end_lineno=1, end_col_offset=5))')
    src = ast.Call(col_offset=1, lineno=1, end_lineno=1, end_col_offset=1)
    new = ast.copy_location(src, ast.Call(col_offset=None, lineno=None))
    self.assertIsNone(new.end_lineno)
    self.assertIsNone(new.end_col_offset)
    self.assertEqual(new.lineno, 1)
    self.assertEqual(new.col_offset, 1)
