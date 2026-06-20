# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class N(ast.Num):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.z = 'spam'

    class N2(ast.Num):
        pass
    n = N(42)
    self.assertEqual(n.n, 42)
    self.assertEqual(n.z, 'spam')
    self.assertEqual(type(n), N)
    self.assertTrue(isinstance(n, N))
    self.assertTrue(isinstance(n, ast.Num))
    self.assertFalse(isinstance(n, N2))
    self.assertFalse(isinstance(ast.Num(42), N))
    n = N(n=42)
    self.assertEqual(n.n, 42)
    self.assertEqual(type(n), N)
