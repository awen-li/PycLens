# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_elif_stmt_start_position

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse('if a:\n    pass\nelif b:\n    pass\n')
    elif_stmt = node.body[0].orelse[0]
    self.assertEqual(elif_stmt.lineno, 3)
    self.assertEqual(elif_stmt.col_offset, 0)
