# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_literal_eval_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ast.literal_eval('6j'), 6j)
    self.assertEqual(ast.literal_eval('-6j'), -6j)
    self.assertEqual(ast.literal_eval('6.75j'), 6.75j)
    self.assertEqual(ast.literal_eval('-6.75j'), -6.75j)
    self.assertEqual(ast.literal_eval('3+6j'), 3 + 6j)
    self.assertEqual(ast.literal_eval('-3+6j'), -3 + 6j)
    self.assertEqual(ast.literal_eval('3-6j'), 3 - 6j)
    self.assertEqual(ast.literal_eval('-3-6j'), -3 - 6j)
    self.assertEqual(ast.literal_eval('3.25+6.75j'), 3.25 + 6.75j)
    self.assertEqual(ast.literal_eval('-3.25+6.75j'), -3.25 + 6.75j)
    self.assertEqual(ast.literal_eval('3.25-6.75j'), 3.25 - 6.75j)
    self.assertEqual(ast.literal_eval('-3.25-6.75j'), -3.25 - 6.75j)
    self.assertEqual(ast.literal_eval('(3+6j)'), 3 + 6j)
    self.assertRaises(ValueError, ast.literal_eval, '-6j+3')
    self.assertRaises(ValueError, ast.literal_eval, '-6j+3j')
    self.assertRaises(ValueError, ast.literal_eval, '3+-6j')
    self.assertRaises(ValueError, ast.literal_eval, '3+(0+6j)')
    self.assertRaises(ValueError, ast.literal_eval, '-(3+6j)')
