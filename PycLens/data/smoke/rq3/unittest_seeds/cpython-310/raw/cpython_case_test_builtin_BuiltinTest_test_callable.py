# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_callable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(callable(len))
    self.assertFalse(callable('a'))
    self.assertTrue(callable(callable))
    self.assertTrue(callable(lambda x, y: x + y))
    self.assertFalse(callable(__builtins__))

    def f():
        pass
    self.assertTrue(callable(f))

    class C1:

        def meth(self):
            pass
    self.assertTrue(callable(C1))
    c = C1()
    self.assertTrue(callable(c.meth))
    self.assertFalse(callable(c))
    c.__call__ = None
    self.assertFalse(callable(c))
    c.__call__ = lambda self: 0
    self.assertFalse(callable(c))
    del c.__call__
    self.assertFalse(callable(c))

    class C2(object):

        def __call__(self):
            pass
    c2 = C2()
    self.assertTrue(callable(c2))
    c2.__call__ = None
    self.assertTrue(callable(c2))

    class C3(C2):
        pass
    c3 = C3()
    self.assertTrue(callable(c3))
