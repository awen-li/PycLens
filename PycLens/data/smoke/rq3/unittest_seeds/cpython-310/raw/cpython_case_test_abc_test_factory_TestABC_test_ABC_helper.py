# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_ABC_helper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(abc.ABC):

        @classmethod
        @abc.abstractmethod
        def foo(cls):
            return cls.__name__
    self.assertEqual(type(C), abc.ABCMeta)
    self.assertRaises(TypeError, C)

    class D(C):

        @classmethod
        def foo(cls):
            return super().foo()
    self.assertEqual(D.foo(), 'D')
