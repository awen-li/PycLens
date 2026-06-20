# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_recursion_direct

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ast.UnaryOp(op=ast.Not(), lineno=0, col_offset=0)
    e.operand = e
    with self.assertRaises(RecursionError):
        with support.infinite_recursion():
            compile(ast.Expression(e), '<test>', 'eval')
