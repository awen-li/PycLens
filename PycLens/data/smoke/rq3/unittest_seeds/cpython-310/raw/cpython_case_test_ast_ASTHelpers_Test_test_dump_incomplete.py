# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_dump_incomplete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.Raise(lineno=3, col_offset=4)
    self.assertEqual(ast.dump(node), 'Raise()')
    self.assertEqual(ast.dump(node, include_attributes=True), 'Raise(lineno=3, col_offset=4)')
    node = ast.Raise(exc=ast.Name(id='e', ctx=ast.Load()), lineno=3, col_offset=4)
    self.assertEqual(ast.dump(node), "Raise(exc=Name(id='e', ctx=Load()))")
    self.assertEqual(ast.dump(node, annotate_fields=False), "Raise(Name('e', Load()))")
    self.assertEqual(ast.dump(node, include_attributes=True), "Raise(exc=Name(id='e', ctx=Load()), lineno=3, col_offset=4)")
    self.assertEqual(ast.dump(node, annotate_fields=False, include_attributes=True), "Raise(Name('e', Load()), lineno=3, col_offset=4)")
    node = ast.Raise(cause=ast.Name(id='e', ctx=ast.Load()))
    self.assertEqual(ast.dump(node), "Raise(cause=Name(id='e', ctx=Load()))")
    self.assertEqual(ast.dump(node, annotate_fields=False), "Raise(cause=Name('e', Load()))")
