# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_AST_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ast.AST()
    self.assertEqual(x._fields, ())
    x.foobar = 42
    self.assertEqual(x.foobar, 42)
    self.assertEqual(x.__dict__['foobar'], 42)
    with self.assertRaises(AttributeError):
        x.vararg
    with self.assertRaises(TypeError):
        ast.AST(2)
