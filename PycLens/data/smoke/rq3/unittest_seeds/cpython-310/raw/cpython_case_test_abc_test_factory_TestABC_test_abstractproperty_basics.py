# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_abstractproperty_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @property
    @abc.abstractmethod
    def foo(self):
        pass
    self.assertTrue(foo.__isabstractmethod__)

    def bar(self):
        pass
    self.assertFalse(getattr(bar, '__isabstractmethod__', False))

    class C(metaclass=abc_ABCMeta):

        @property
        @abc.abstractmethod
        def foo(self):
            return 3
    self.assertRaises(TypeError, C)

    class D(C):

        @C.foo.getter
        def foo(self):
            return super().foo
    self.assertEqual(D().foo, 3)
