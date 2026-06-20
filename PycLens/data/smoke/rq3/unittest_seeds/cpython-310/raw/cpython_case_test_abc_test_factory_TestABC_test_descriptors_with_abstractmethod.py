# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_descriptors_with_abstractmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(metaclass=abc_ABCMeta):

        @property
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
    self.assertEqual(E().foo, 3)

    class NotBool(object):

        def __bool__(self):
            raise ValueError()
        __len__ = __bool__
    with self.assertRaises(ValueError):

        class F(C):

            def bar(self):
                pass
            bar.__isabstractmethod__ = NotBool()
            foo = property(bar)
