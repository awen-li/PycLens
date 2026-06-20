# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ast.arguments()
    self.assertEqual(x._fields, ('posonlyargs', 'args', 'vararg', 'kwonlyargs', 'kw_defaults', 'kwarg', 'defaults'))
    with self.assertRaises(AttributeError):
        x.args
    self.assertIsNone(x.vararg)
    x = ast.arguments(*range(1, 8))
    self.assertEqual(x.args, 2)
    self.assertEqual(x.vararg, 3)
