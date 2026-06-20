# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_starred_expr_end_position_within_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse('f(*[0, 1])')
    starred_expr = node.body[0].value.args[0]
    self.assertEqual(starred_expr.end_lineno, 1)
    self.assertEqual(starred_expr.end_col_offset, 9)
