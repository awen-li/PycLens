# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestPredicates_test_isabstract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from abc import ABCMeta, abstractmethod

    class AbstractClassExample(metaclass=ABCMeta):

        @abstractmethod
        def foo(self):
            pass

    class ClassExample(AbstractClassExample):

        def foo(self):
            pass
    a = ClassExample()
    self.assertTrue(inspect.isabstract(AbstractClassExample))
    self.assertFalse(inspect.isabstract(ClassExample))
    self.assertFalse(inspect.isabstract(a))
    self.assertFalse(inspect.isabstract(int))
    self.assertFalse(inspect.isabstract(5))
