# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_literal_eval_trailing_ws

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ast.literal_eval('    -1'), -1)
    self.assertEqual(ast.literal_eval('\t\t-1'), -1)
    self.assertEqual(ast.literal_eval(' \t -1'), -1)
    self.assertRaises(IndentationError, ast.literal_eval, '\n -1')
