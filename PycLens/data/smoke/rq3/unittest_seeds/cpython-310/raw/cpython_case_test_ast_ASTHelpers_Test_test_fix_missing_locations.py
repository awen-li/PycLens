# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_fix_missing_locations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = ast.parse('write("spam")')
    src.body.append(ast.Expr(ast.Call(ast.Name('spam', ast.Load()), [ast.Str('eggs')], [])))
    self.assertEqual(src, ast.fix_missing_locations(src))
    self.maxDiff = None
    self.assertEqual(ast.dump(src, include_attributes=True), "Module(body=[Expr(value=Call(func=Name(id='write', ctx=Load(), lineno=1, col_offset=0, end_lineno=1, end_col_offset=5), args=[Constant(value='spam', lineno=1, col_offset=6, end_lineno=1, end_col_offset=12)], keywords=[], lineno=1, col_offset=0, end_lineno=1, end_col_offset=13), lineno=1, col_offset=0, end_lineno=1, end_col_offset=13), Expr(value=Call(func=Name(id='spam', ctx=Load(), lineno=1, col_offset=0, end_lineno=1, end_col_offset=0), args=[Constant(value='eggs', lineno=1, col_offset=0, end_lineno=1, end_col_offset=0)], keywords=[], lineno=1, col_offset=0, end_lineno=1, end_col_offset=0), lineno=1, col_offset=0, end_lineno=1, end_col_offset=0)], type_ignores=[])")
