# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_update_new_abstractmethods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def bar(self):
            pass

    @abc.abstractmethod
    def updated_foo(self):
        pass
    A.foo = updated_foo
    abc.update_abstractmethods(A)
    self.assertEqual(A.__abstractmethods__, {'foo', 'bar'})
    msg = 'class A with abstract methods bar, foo'
    self.assertRaisesRegex(TypeError, msg, A)
