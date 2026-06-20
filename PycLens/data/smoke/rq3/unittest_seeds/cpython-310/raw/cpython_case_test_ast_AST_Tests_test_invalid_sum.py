# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_invalid_sum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pos = dict(lineno=2, col_offset=3)
    m = ast.Module([ast.Expr(ast.expr(**pos), **pos)], [])
    with self.assertRaises(TypeError) as cm:
        compile(m, '<test>', 'exec')
    self.assertIn('but got <ast.expr', str(cm.exception))
