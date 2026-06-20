# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_invalid_constant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for invalid_constant in (int, (1, 2, int), frozenset((1, 2, int))):
        e = ast.Expression(body=ast.Constant(invalid_constant))
        ast.fix_missing_locations(e)
        with self.assertRaisesRegex(TypeError, 'invalid type in Constant: type'):
            compile(e, '<test>', 'eval')
