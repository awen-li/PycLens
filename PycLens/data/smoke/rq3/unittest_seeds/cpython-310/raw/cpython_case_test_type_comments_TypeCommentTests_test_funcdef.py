# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_comments.py
# case: TypeCommentTests_test_funcdef

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tree in self.parse_all(funcdef):
        self.assertEqual(tree.body[0].type_comment, '() -> int')
        self.assertEqual(tree.body[1].type_comment, '() -> None')
    tree = self.classic_parse(funcdef)
    self.assertEqual(tree.body[0].type_comment, None)
    self.assertEqual(tree.body[1].type_comment, None)
