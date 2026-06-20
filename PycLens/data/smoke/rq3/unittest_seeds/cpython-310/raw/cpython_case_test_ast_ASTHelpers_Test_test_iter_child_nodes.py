# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_iter_child_nodes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse("spam(23, 42, eggs='leek')", mode='eval')
    self.assertEqual(len(list(ast.iter_child_nodes(node.body))), 4)
    iterator = ast.iter_child_nodes(node.body)
    self.assertEqual(next(iterator).id, 'spam')
    self.assertEqual(next(iterator).value, 23)
    self.assertEqual(next(iterator).value, 42)
    self.assertEqual(ast.dump(next(iterator)), "keyword(arg='eggs', value=Constant(value='leek'))")
