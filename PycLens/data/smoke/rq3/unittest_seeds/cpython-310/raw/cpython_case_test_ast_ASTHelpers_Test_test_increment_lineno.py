# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_increment_lineno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = ast.parse('1 + 1', mode='eval')
    self.assertEqual(ast.increment_lineno(src, n=3), src)
    self.assertEqual(ast.dump(src, include_attributes=True), 'Expression(body=BinOp(left=Constant(value=1, lineno=4, col_offset=0, end_lineno=4, end_col_offset=1), op=Add(), right=Constant(value=1, lineno=4, col_offset=4, end_lineno=4, end_col_offset=5), lineno=4, col_offset=0, end_lineno=4, end_col_offset=5))')
    src = ast.parse('1 + 1', mode='eval')
    self.assertEqual(ast.increment_lineno(src.body, n=3), src.body)
    self.assertEqual(ast.dump(src, include_attributes=True), 'Expression(body=BinOp(left=Constant(value=1, lineno=4, col_offset=0, end_lineno=4, end_col_offset=1), op=Add(), right=Constant(value=1, lineno=4, col_offset=4, end_lineno=4, end_col_offset=5), lineno=4, col_offset=0, end_lineno=4, end_col_offset=5))')
    src = ast.Call(func=ast.Name('test', ast.Load()), args=[], keywords=[], lineno=1)
    self.assertEqual(ast.increment_lineno(src).lineno, 2)
    self.assertIsNone(ast.increment_lineno(src).end_lineno)
