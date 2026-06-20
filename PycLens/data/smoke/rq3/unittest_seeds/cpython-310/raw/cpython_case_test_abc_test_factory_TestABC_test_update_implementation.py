# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_update_implementation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def foo(self):
            pass

    class B(A):
        pass
    msg = 'class B with abstract method foo'
    self.assertRaisesRegex(TypeError, msg, B)
    self.assertEqual(B.__abstractmethods__, {'foo'})
    B.foo = lambda self: None
    abc.update_abstractmethods(B)
    B()
    self.assertEqual(B.__abstractmethods__, set())
