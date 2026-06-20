# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_staticmethod_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        @functools.singledispatchmethod
        @staticmethod
        def t(arg):
            return arg

        @t.register(int)
        @staticmethod
        def _(arg):
            return isinstance(arg, int)

        @t.register(str)
        @staticmethod
        def _(arg):
            return isinstance(arg, str)
    a = A()
    self.assertTrue(A.t(0))
    self.assertTrue(A.t(''))
    self.assertEqual(A.t(0.0), 0.0)
