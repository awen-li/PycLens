# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_update_multi_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def foo(self):
            pass

    class B(metaclass=abc_ABCMeta):

        def foo(self):
            pass

    class C(B, A):

        @abc.abstractmethod
        def foo(self):
            pass
    self.assertEqual(C.__abstractmethods__, {'foo'})
    del C.foo
    abc.update_abstractmethods(C)
    self.assertEqual(C.__abstractmethods__, set())
    C()
