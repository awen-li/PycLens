# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_comments.py
# case: TypeCommentTests_test_withstmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tree in self.parse_all(withstmt):
        self.assertEqual(tree.body[0].type_comment, 'int')
    tree = self.classic_parse(withstmt)
    self.assertEqual(tree.body[0].type_comment, None)
