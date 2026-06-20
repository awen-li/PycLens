# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_positional_only_feature_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ast.parse('def foo(x, /): ...', feature_version=(3, 8))
    ast.parse('def bar(x=1, /): ...', feature_version=(3, 8))
    with self.assertRaises(SyntaxError):
        ast.parse('def foo(x, /): ...', feature_version=(3, 7))
    with self.assertRaises(SyntaxError):
        ast.parse('def bar(x=1, /): ...', feature_version=(3, 7))
    ast.parse('lambda x, /: ...', feature_version=(3, 8))
    ast.parse('lambda x=1, /: ...', feature_version=(3, 8))
    with self.assertRaises(SyntaxError):
        ast.parse('lambda x, /: ...', feature_version=(3, 7))
    with self.assertRaises(SyntaxError):
        ast.parse('lambda x=1, /: ...', feature_version=(3, 7))
