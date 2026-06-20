# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_alias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    im = ast.parse('from bar import y').body[0]
    self.assertEqual(len(im.names), 1)
    alias = im.names[0]
    self.assertEqual(alias.name, 'y')
    self.assertIsNone(alias.asname)
    self.assertEqual(alias.lineno, 1)
    self.assertEqual(alias.end_lineno, 1)
    self.assertEqual(alias.col_offset, 16)
    self.assertEqual(alias.end_col_offset, 17)
    im = ast.parse('from bar import *').body[0]
    alias = im.names[0]
    self.assertEqual(alias.name, '*')
    self.assertIsNone(alias.asname)
    self.assertEqual(alias.lineno, 1)
    self.assertEqual(alias.end_lineno, 1)
    self.assertEqual(alias.col_offset, 16)
    self.assertEqual(alias.end_col_offset, 17)
    im = ast.parse('from bar import y as z').body[0]
    alias = im.names[0]
    self.assertEqual(alias.name, 'y')
    self.assertEqual(alias.asname, 'z')
    self.assertEqual(alias.lineno, 1)
    self.assertEqual(alias.end_lineno, 1)
    self.assertEqual(alias.col_offset, 16)
    self.assertEqual(alias.end_col_offset, 22)
    im = ast.parse('import bar as foo').body[0]
    alias = im.names[0]
    self.assertEqual(alias.name, 'bar')
    self.assertEqual(alias.asname, 'foo')
    self.assertEqual(alias.lineno, 1)
    self.assertEqual(alias.end_lineno, 1)
    self.assertEqual(alias.col_offset, 7)
    self.assertEqual(alias.end_col_offset, 17)
