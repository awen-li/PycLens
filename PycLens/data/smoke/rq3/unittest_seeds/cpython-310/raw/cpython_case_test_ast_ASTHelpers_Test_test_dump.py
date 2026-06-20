# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_dump

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse('spam(eggs, "and cheese")')
    self.assertEqual(ast.dump(node), "Module(body=[Expr(value=Call(func=Name(id='spam', ctx=Load()), args=[Name(id='eggs', ctx=Load()), Constant(value='and cheese')], keywords=[]))], type_ignores=[])")
    self.assertEqual(ast.dump(node, annotate_fields=False), "Module([Expr(Call(Name('spam', Load()), [Name('eggs', Load()), Constant('and cheese')], []))], [])")
    self.assertEqual(ast.dump(node, include_attributes=True), "Module(body=[Expr(value=Call(func=Name(id='spam', ctx=Load(), lineno=1, col_offset=0, end_lineno=1, end_col_offset=4), args=[Name(id='eggs', ctx=Load(), lineno=1, col_offset=5, end_lineno=1, end_col_offset=9), Constant(value='and cheese', lineno=1, col_offset=11, end_lineno=1, end_col_offset=23)], keywords=[], lineno=1, col_offset=0, end_lineno=1, end_col_offset=24), lineno=1, col_offset=0, end_lineno=1, end_col_offset=24)], type_ignores=[])")
