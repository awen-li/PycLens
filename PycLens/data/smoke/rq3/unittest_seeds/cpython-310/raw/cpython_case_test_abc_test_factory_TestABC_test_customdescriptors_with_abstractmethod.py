# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_customdescriptors_with_abstractmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descriptor:

        def __init__(self, fget, fset=None):
            self._fget = fget
            self._fset = fset

        def getter(self, callable):
            return Descriptor(callable, self._fget)

        def setter(self, callable):
            return Descriptor(self._fget, callable)

        @property
        def __isabstractmethod__(self):
            return getattr(self._fget, '__isabstractmethod__', False) or getattr(self._fset, '__isabstractmethod__', False)

    class C(metaclass=abc_ABCMeta):

        @Descriptor
        @abc.abstractmethod
        def foo(self):
            return 3

        @foo.setter
        @abc.abstractmethod
        def foo(self, val):
            pass
    self.assertRaises(TypeError, C)

    class D(C):

        @C.foo.getter
        def foo(self):
            return super().foo
    self.assertRaises(TypeError, D)

    class E(D):

        @D.foo.setter
        def foo(self, val):
            pass
    self.assertFalse(E.foo.__isabstractmethod__)
