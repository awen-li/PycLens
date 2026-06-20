# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_abstractmethod_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @abc.abstractmethod
    def foo(self):
        pass
    self.assertTrue(foo.__isabstractmethod__)

    def bar(self):
        pass
    self.assertFalse(hasattr(bar, '__isabstractmethod__'))
