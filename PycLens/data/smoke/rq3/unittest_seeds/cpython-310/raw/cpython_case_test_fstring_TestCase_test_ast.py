# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_ast

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __init__(self):
            self.called = False

        def __call__(self):
            self.called = True
            return 4
    x = X()
    expr = "\na = 10\nf'{a * x()}'"
    t = ast.parse(expr)
    c = compile(t, '', 'exec')
    self.assertFalse(x.called)
    exec(c)
    self.assertTrue(x.called)
