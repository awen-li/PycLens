# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartialMethod_test_abstract

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Abstract(abc.ABCMeta):

        @abc.abstractmethod
        def add(self, x, y):
            pass
        add5 = functools.partialmethod(add, 5)
    self.assertTrue(Abstract.add.__isabstractmethod__)
    self.assertTrue(Abstract.add5.__isabstractmethod__)
    for func in [self.A.static, self.A.cls, self.A.over_partial, self.A.nested, self.A.both]:
        self.assertFalse(getattr(func, '__isabstractmethod__', False))
