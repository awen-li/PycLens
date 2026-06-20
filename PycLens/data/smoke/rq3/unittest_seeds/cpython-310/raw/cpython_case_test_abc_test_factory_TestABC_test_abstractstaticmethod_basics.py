# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_abstractstaticmethod_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @staticmethod
    @abc.abstractmethod
    def foo():
        pass
    self.assertTrue(foo.__isabstractmethod__)

    @staticmethod
    def bar():
        pass
    self.assertFalse(getattr(bar, '__isabstractmethod__', False))

    class C(metaclass=abc_ABCMeta):

        @staticmethod
        @abc.abstractmethod
        def foo():
            return 3
    self.assertRaises(TypeError, C)

    class D(C):

        @staticmethod
        def foo():
            return 4
    self.assertEqual(D.foo(), 4)
    self.assertEqual(D().foo(), 4)
