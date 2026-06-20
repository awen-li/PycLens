# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_subclasshook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc.ABCMeta):

        @classmethod
        def __subclasshook__(cls, C):
            if cls is A:
                return 'foo' in C.__dict__
            return NotImplemented
    self.assertFalse(issubclass(A, A))
    self.assertFalse(issubclass(A, (A,)))

    class B:
        foo = 42
    self.assertTrue(issubclass(B, A))
    self.assertTrue(issubclass(B, (A,)))

    class C:
        spam = 42
    self.assertFalse(issubclass(C, A))
    self.assertFalse(issubclass(C, (A,)))
