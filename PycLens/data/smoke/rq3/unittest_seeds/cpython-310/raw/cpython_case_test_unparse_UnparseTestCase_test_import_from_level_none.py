# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_import_from_level_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ast.ImportFrom(module='mod', names=[ast.alias(name='x')])
    self.assertEqual(ast.unparse(tree), 'from mod import x')
    tree = ast.ImportFrom(module='mod', names=[ast.alias(name='x')], level=None)
    self.assertEqual(ast.unparse(tree), 'from mod import x')
