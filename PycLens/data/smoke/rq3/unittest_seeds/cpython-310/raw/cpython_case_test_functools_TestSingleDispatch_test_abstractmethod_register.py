# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_abstractmethod_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Abstract(metaclass=abc.ABCMeta):

        @functools.singledispatchmethod
        @abc.abstractmethod
        def add(self, x, y):
            pass
    self.assertTrue(Abstract.add.__isabstractmethod__)
    self.assertTrue(Abstract.__dict__['add'].__isabstractmethod__)
    with self.assertRaises(TypeError):
        Abstract()
