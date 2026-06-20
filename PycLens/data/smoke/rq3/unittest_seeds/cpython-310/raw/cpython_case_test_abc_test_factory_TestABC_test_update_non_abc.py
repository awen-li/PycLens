# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_update_non_abc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass

    @abc.abstractmethod
    def updated_foo(self):
        pass
    A.foo = updated_foo
    abc.update_abstractmethods(A)
    A()
    self.assertFalse(hasattr(A, '__abstractmethods__'))
