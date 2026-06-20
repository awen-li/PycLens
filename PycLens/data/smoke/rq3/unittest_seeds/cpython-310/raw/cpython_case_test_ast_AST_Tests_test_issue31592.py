# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_issue31592

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import unicodedata

    def bad_normalize(*args):
        return None
    with support.swap_attr(unicodedata, 'normalize', bad_normalize):
        self.assertRaises(TypeError, ast.parse, 'ϕ')
