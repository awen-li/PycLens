# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_registration_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(metaclass=abc_ABCMeta):
        pass

    class B(object):
        pass
    b = B()
    self.assertFalse(issubclass(B, A))
    self.assertFalse(issubclass(B, (A,)))
    self.assertNotIsInstance(b, A)
    self.assertNotIsInstance(b, (A,))
    B1 = A.register(B)
    self.assertTrue(issubclass(B, A))
    self.assertTrue(issubclass(B, (A,)))
    self.assertIsInstance(b, A)
    self.assertIsInstance(b, (A,))
    self.assertIs(B1, B)

    class C(B):
        pass
    c = C()
    self.assertTrue(issubclass(C, A))
    self.assertTrue(issubclass(C, (A,)))
    self.assertIsInstance(c, A)
    self.assertIsInstance(c, (A,))
