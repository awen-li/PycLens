# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_literal_eval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ast.literal_eval('[1, 2, 3]'), [1, 2, 3])
    self.assertEqual(ast.literal_eval('{"foo": 42}'), {'foo': 42})
    self.assertEqual(ast.literal_eval('(True, False, None)'), (True, False, None))
    self.assertEqual(ast.literal_eval('{1, 2, 3}'), {1, 2, 3})
    self.assertEqual(ast.literal_eval('b"hi"'), b'hi')
    self.assertEqual(ast.literal_eval('set()'), set())
    self.assertRaises(ValueError, ast.literal_eval, 'foo()')
    self.assertEqual(ast.literal_eval('6'), 6)
    self.assertEqual(ast.literal_eval('+6'), 6)
    self.assertEqual(ast.literal_eval('-6'), -6)
    self.assertEqual(ast.literal_eval('3.25'), 3.25)
    self.assertEqual(ast.literal_eval('+3.25'), 3.25)
    self.assertEqual(ast.literal_eval('-3.25'), -3.25)
    self.assertEqual(repr(ast.literal_eval('-0.0')), '-0.0')
    self.assertRaises(ValueError, ast.literal_eval, '++6')
    self.assertRaises(ValueError, ast.literal_eval, '+True')
    self.assertRaises(ValueError, ast.literal_eval, '2+3')
