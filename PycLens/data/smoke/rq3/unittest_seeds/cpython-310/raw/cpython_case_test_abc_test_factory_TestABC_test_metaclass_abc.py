# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_metaclass_abc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):

        @abc.abstractmethod
        def x(self):
            pass
    self.assertEqual(A.__abstractmethods__, {'x'})

    class meta(type, A):

        def x(self):
            return 1

    class C(metaclass=meta):
        pass
