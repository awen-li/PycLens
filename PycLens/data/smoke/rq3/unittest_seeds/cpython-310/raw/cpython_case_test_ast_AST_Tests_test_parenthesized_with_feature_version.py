# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_parenthesized_with_feature_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ast.parse('with (CtxManager() as example): ...', feature_version=(3, 10))
    ast.parse('with (CtxManager() as example): ...', feature_version=(3, 9))
    with self.assertRaises(SyntaxError):
        ast.parse('with (CtxManager() as example): ...', feature_version=(3, 8))
    ast.parse('with CtxManager() as example: ...', feature_version=(3, 8))
