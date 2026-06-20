# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_get_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ast.parse("'docstring'\nx = 1")
    self.assertEqual(ast.get_docstring(tree), 'docstring')
