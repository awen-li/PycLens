# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_get_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse('"""line one\n  line two"""')
    self.assertEqual(ast.get_docstring(node), 'line one\nline two')
    node = ast.parse('class foo:\n  """line one\n  line two"""')
    self.assertEqual(ast.get_docstring(node.body[0]), 'line one\nline two')
    node = ast.parse('def foo():\n  """line one\n  line two"""')
    self.assertEqual(ast.get_docstring(node.body[0]), 'line one\nline two')
    node = ast.parse('async def foo():\n  """spam\n  ham"""')
    self.assertEqual(ast.get_docstring(node.body[0]), 'spam\nham')
