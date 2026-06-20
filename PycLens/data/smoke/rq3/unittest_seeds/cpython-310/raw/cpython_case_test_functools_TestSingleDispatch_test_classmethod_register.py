# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_classmethod_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __init__(self, arg):
            self.arg = arg

        @functools.singledispatchmethod
        @classmethod
        def t(cls, arg):
            return cls('base')

        @t.register(int)
        @classmethod
        def _(cls, arg):
            return cls('int')

        @t.register(str)
        @classmethod
        def _(cls, arg):
            return cls('str')
    self.assertEqual(A.t(0).arg, 'int')
    self.assertEqual(A.t('').arg, 'str')
    self.assertEqual(A.t(0.0).arg, 'base')
