# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_update_del

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def foo(self):
            pass
    del A.foo
    self.assertEqual(A.__abstractmethods__, {'foo'})
    self.assertFalse(hasattr(A, 'foo'))
    abc.update_abstractmethods(A)
    self.assertEqual(A.__abstractmethods__, set())
    A()
