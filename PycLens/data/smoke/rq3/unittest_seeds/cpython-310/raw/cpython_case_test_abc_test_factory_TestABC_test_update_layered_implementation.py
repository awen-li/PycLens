# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_update_layered_implementation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def foo(self):
            pass

    class B(A):
        pass

    class C(B):

        def foo(self):
            pass
    C()
    del C.foo
    abc.update_abstractmethods(C)
    msg = 'class C with abstract method foo'
    self.assertRaisesRegex(TypeError, msg, C)
