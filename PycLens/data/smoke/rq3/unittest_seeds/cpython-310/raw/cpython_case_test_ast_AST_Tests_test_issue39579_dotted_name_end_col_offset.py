# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_issue39579_dotted_name_end_col_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ast.parse('@a.b.c\ndef f(): pass')
    attr_b = tree.body[0].decorator_list[0].value
    self.assertEqual(attr_b.end_col_offset, 4)
