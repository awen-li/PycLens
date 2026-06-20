# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_abstractclassmethod_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @classmethod
    @abc.abstractmethod
    def foo(cls):
        pass
    self.assertTrue(foo.__isabstractmethod__)

    @classmethod
    def bar(cls):
        pass
    self.assertFalse(getattr(bar, '__isabstractmethod__', False))

    class C(metaclass=abc_ABCMeta):

        @classmethod
        @abc.abstractmethod
        def foo(cls):
            return cls.__name__
    self.assertRaises(TypeError, C)

    class D(C):

        @classmethod
        def foo(cls):
            return super().foo()
    self.assertEqual(D.foo(), 'D')
    self.assertEqual(D().foo(), 'D')
