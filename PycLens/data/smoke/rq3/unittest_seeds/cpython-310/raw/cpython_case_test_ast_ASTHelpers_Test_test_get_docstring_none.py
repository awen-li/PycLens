# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_get_docstring_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsNone(ast.get_docstring(ast.parse('')))
    node = ast.parse('x = "not docstring"')
    self.assertIsNone(ast.get_docstring(node))
    node = ast.parse('def foo():\n  pass')
    self.assertIsNone(ast.get_docstring(node))
    node = ast.parse('class foo:\n  pass')
    self.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('class foo:\n  x = "not docstring"')
    self.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('class foo:\n  def bar(self): pass')
    self.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('def foo():\n  pass')
    self.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('def foo():\n  x = "not docstring"')
    self.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('async def foo():\n  pass')
    self.assertIsNone(ast.get_docstring(node.body[0]))
    node = ast.parse('async def foo():\n  x = "not docstring"')
    self.assertIsNone(ast.get_docstring(node.body[0]))
