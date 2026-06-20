# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_update_as_decorator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def foo(self):
            pass

    def class_decorator(cls):
        cls.foo = lambda self: None
        return cls

    @abc.update_abstractmethods
    @class_decorator
    class B(A):
        pass
    B()
    self.assertEqual(B.__abstractmethods__, set())
