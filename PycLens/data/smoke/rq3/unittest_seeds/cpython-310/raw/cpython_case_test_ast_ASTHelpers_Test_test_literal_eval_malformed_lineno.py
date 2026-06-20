# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_literal_eval_malformed_lineno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'malformed node or string on line 3:'
    with self.assertRaisesRegex(ValueError, msg):
        ast.literal_eval("{'a': 1,\n'b':2,\n'c':++3,\n'd':4}")
    node = ast.UnaryOp(ast.UAdd(), ast.UnaryOp(ast.UAdd(), ast.Constant(6)))
    self.assertIsNone(getattr(node, 'lineno', None))
    msg = 'malformed node or string:'
    with self.assertRaisesRegex(ValueError, msg):
        ast.literal_eval(node)
