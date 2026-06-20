# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestLegacyAPI_test_abstractproperty_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @abc.abstractproperty
    def foo(self):
        pass
    self.assertTrue(foo.__isabstractmethod__)

    def bar(self):
        pass
    self.assertFalse(hasattr(bar, '__isabstractmethod__'))

    class C(metaclass=abc_ABCMeta):

        @abc.abstractproperty
        def foo(self):
            return 3
    self.assertRaises(TypeError, C)

    class D(C):

        @property
        def foo(self):
            return super().foo
    self.assertEqual(D().foo, 3)
    self.assertFalse(getattr(D.foo, '__isabstractmethod__', False))
