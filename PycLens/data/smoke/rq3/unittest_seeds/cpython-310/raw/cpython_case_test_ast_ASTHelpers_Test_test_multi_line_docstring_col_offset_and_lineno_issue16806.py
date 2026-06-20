# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_multi_line_docstring_col_offset_and_lineno_issue16806

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse('"""line one\nline two"""\n\ndef foo():\n  """line one\n  line two"""\n\n  def bar():\n    """line one\n    line two"""\n  """line one\n  line two"""\n"""line one\nline two"""\n\n')
    self.assertEqual(node.body[0].col_offset, 0)
    self.assertEqual(node.body[0].lineno, 1)
    self.assertEqual(node.body[1].body[0].col_offset, 2)
    self.assertEqual(node.body[1].body[0].lineno, 5)
    self.assertEqual(node.body[1].body[1].body[0].col_offset, 4)
    self.assertEqual(node.body[1].body[1].body[0].lineno, 9)
    self.assertEqual(node.body[1].body[2].col_offset, 2)
    self.assertEqual(node.body[1].body[2].lineno, 11)
    self.assertEqual(node.body[2].col_offset, 0)
    self.assertEqual(node.body[2].lineno, 13)
