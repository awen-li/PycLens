# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestPredicates_test_isabstract_during_init_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from abc import ABCMeta, abstractmethod
    isabstract_checks = []

    class AbstractChecker(metaclass=ABCMeta):

        def __init_subclass__(cls):
            isabstract_checks.append(inspect.isabstract(cls))

    class AbstractClassExample(AbstractChecker):

        @abstractmethod
        def foo(self):
            pass

    class ClassExample(AbstractClassExample):

        def foo(self):
            pass
    self.assertEqual(isabstract_checks, [True, False])
    isabstract_checks.clear()

    class AbstractChild(AbstractClassExample):
        pass

    class AbstractGrandchild(AbstractChild):
        pass

    class ConcreteGrandchild(ClassExample):
        pass
    self.assertEqual(isabstract_checks, [True, True, False])
